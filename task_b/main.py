from typing import List
from const import (MIN_COUNT, DOT, ROWS_COUNT, COLS_COUNT, MAX_COUNT,
                   SPACE, MIN_DATA_LEN, MAX_DATA_LEN, ALPHABET, WRONG_DATA_LEN_ERROR_MSG,
                   WRONG_DATA_FORMAT_ERROR_MSG, WRONG_NUMBER_MSG, WRONG_RANGE_MSG)

def get_count() -> int:
    count = input()
    if not count.isnumeric():
        raise ValueError(WRONG_NUMBER_MSG.format(count))
    count = int(count)
    if not MIN_COUNT <= count <= MAX_COUNT:
        raise ValueError(WRONG_RANGE_MSG.format(count))
    return count

def check_format(text: str) -> None:
    if not MIN_DATA_LEN <= len(text) <= MAX_DATA_LEN:
        raise ValueError(WRONG_DATA_LEN_ERROR_MSG.format(text))

    if not bool(text) or not all(char in ALPHABET for char in text):
        raise ValueError(WRONG_DATA_FORMAT_ERROR_MSG.format(text))


def get_items(count: int) -> List[str]:
    items = []
    for _ in range(count):
        input_data = input()
        check_format(input_data)
        items.append(input_data)
    return items


def get_prog_matrix(items: List[str]) -> List[List[str]]:
    first_letters = {item[0] for item in items}
    prog_list = [char if char in first_letters else DOT for char in ALPHABET]

    while len(prog_list) < ROWS_COUNT * COLS_COUNT:
        prog_list.append(SPACE)

    prog_matrix = []

    for i in range(ROWS_COUNT):
        row = prog_list[(i * COLS_COUNT) : ((i + 1) * COLS_COUNT)]
        prog_matrix.append(row)

    return prog_matrix


def print_prod_matrix(matrix) -> None:
    for row in matrix:
        for col in row:
            print(col, end=SPACE)
        print()


if __name__ == "__main__":
    try:
        user_count = get_count()
        user_items = get_items(user_count)
        print()

        user_prog_matrix = get_prog_matrix(user_items)
        print_prod_matrix(user_prog_matrix)
        print()
    except ValueError as ve:
        print(ve)
