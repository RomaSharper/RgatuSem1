from typing import List, Callable, Optional, Any


def get_args(args: List[str], request_flag: str,
             validator: Optional[Callable] = None,
             mapper: Optional[Callable[[str], Any]] = None,
             splitter: str = ",", debug: bool = False) -> Optional[List[Any]]:
    """
    Парсит аргументы с маппингом и валидацией.

    Порядок: mapper(если есть) → validator(если есть) → результат
    """
    if len(args) != 3:
        return None

    _, flag, raw = args
    if flag != request_flag:
        return None

    raw = raw.strip()
    if debug:
        print(f"[{request_flag}] '{raw}'")

    if not raw:
        return []

    parts = [part.strip() for part in raw.split(splitter) if part.strip()]
    if not parts:
        return None

    value: Any = None
    items: List[Any] = []
    for part in parts:
        try:
            # 1. Маппер (если есть)
            value = mapper(part) if mapper else part

            # 2. Валидатор (если есть) — работает с результатом маппера
            if validator:
                validator(value)

            items.append(value)
        except (ValueError, TypeError):
            if debug:
                print(f"[{request_flag}] Ошибка '{part}' → {value}")
            return None

    if debug:
        print(f"[{request_flag}] ✓ {items}")
    return items
