from typing import List, Optional
import sys

from common.args_parser import get_args
from task_b.const import (
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
    count = input("Количество: ").strip()
    if not count.isnumeric():
        raise ValueError(WRONG_NUMBER_MSG.format(count))
    count_int = int(count)
    if not MIN_COUNT <= count_int <= MAX_COUNT:
        raise ValueError(WRONG_RANGE_MSG.format(count_int))
    return count_int


def check_format(text: str) -> None:
    if not (MIN_DATA_LEN <= len(text) <= MAX_DATA_LEN):
        raise ValueError(WRONG_DATA_LEN_ERROR_MSG.format(text))

    if not text or not all(char in ALPHABET for char in text):
        raise ValueError(WRONG_DATA_FORMAT_ERROR_MSG.format(text))


def get_items_from_input(count: int) -> List[str]:
    print("Ввод параметров:")
    items: List[str] = []
    for _ in range(count):
        input_data = input().strip()
        check_format(input_data)
        items.append(input_data)
    return items


def get_items_from_argv(argv: List[str]) -> Optional[List[str]]:
    return get_args(argv, "/items", debug=True)


def get_prog_matrix(items: List[str]) -> List[List[str]]:
    first_letters = {item[0] for item in items}
    prog_list = [char if char in first_letters else DOT for char in ALPHABET]

    while len(prog_list) < ROWS_COUNT * COLS_COUNT:
        prog_list.append(SPACE)

    prog_matrix: List[List[str]] = []
    for i in range(ROWS_COUNT):
        row = prog_list[i * COLS_COUNT : (i + 1) * COLS_COUNT]
        prog_matrix.append(row)

    return prog_matrix


def print_prog_matrix(matrix: List[List[str]]) -> None:
    for row in matrix:
        for col in row:
            print(col, end=SPACE)
        print()


def main() -> None:
    argv = sys.argv
    try:
        items = get_items_from_argv(argv) or get_items_from_input(get_count())
        prog_matrix = get_prog_matrix(items)
        print_prog_matrix(prog_matrix)
        print()
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
