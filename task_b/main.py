from typing import List

from const import (
    MIN_COUNT,
    DOT,
    ROWS_COUNT,
    COLS_COUNT,
    MAX_COUNT,
    SPACE,
    MIN_DATA_LEN,
    MAX_DATA_LEN,
    ALPHABET,
    WRONG_DATA_LEN_ERROR_MSG,
    WRONG_DATA_FORMAT_ERROR_MSG,
    WRONG_NUMBER_MSG,
    WRONG_RANGE_MSG,
)


def get_count() -> int:
    count = input().strip()
    if not count.isnumeric():
        raise ValueError(WRONG_NUMBER_MSG.format(count))
    count = int(count)
    if not MIN_COUNT <= count <= MAX_COUNT:
        raise ValueError(WRONG_RANGE_MSG.format(count))
    return count


def check_format(text: str) -> None:
    if not MIN_DATA_LEN <= len(text) <= MAX_DATA_LEN:
        raise ValueError(WRONG_DATA_LEN_ERROR_MSG.format(text))
    if not all(char in ALPHABET for char in text):
        raise ValueError(WRONG_DATA_FORMAT_ERROR_MSG.format(text))


def get_items_from_input(count: int) -> List[str]:
    items: List[str] = []
    for _ in range(count):
        input_data = input().strip()
        check_format(input_data)
        items.append(input_data)
    return items


def get_prog_matrix(items: List[str]) -> List[List[str]]:
    first_letters = {item[0] for item in items}

    prog_matrix: List[List[str]] = []
    for i in range(ROWS_COUNT):
        row = []
        for j in range(COLS_COUNT):
            index = i * COLS_COUNT + j
            if index < len(ALPHABET):
                char = ALPHABET[index]
                row.append(char if char in first_letters else DOT)
        prog_matrix.append(row)

    return prog_matrix

def print_prog_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        print(SPACE.join(row))


def main() -> None:
    try:
        print("Ввод:")
        items = get_items_from_input(get_count())
        print("\nВывод:")
        print_prog_matrix(get_prog_matrix(items))
    except ValueError as ve:
        print("\nОшибка:")
        print(ve)


if __name__ == "__main__":
    main()
