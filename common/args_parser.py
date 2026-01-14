from typing import List, Callable, Optional, Any

RED_END = '\033[0m'
RED_START = '\033[91m'

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
            # 1. Маппер (опционально)
            value = mapper(part) if mapper else part

            # 2. Валидатор (опционально)
            if validator:
                validator(value)

            items.append(value)
        except (ValueError, TypeError) as e:
            error = f"[{request_flag}] {e}"
            if not debug:
                raise_value_error(error)
            print(RED_START, error, RED_END)
            return None

    if debug:
        print(f"[{request_flag}] Успех: {items}")
    return items


def raise_value_error(message: str):
    raise ValueError(f"{RED_START} {message} {RED_END}")
