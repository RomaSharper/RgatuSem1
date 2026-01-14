from typing import List, Optional
import sys
from functools import lru_cache
from task_m.color import Color
from common.args_parser import get_args, raise_value_error

MOD = 998244353


def validate_count(count: int):
    if count < 1 or count > 10 ** 5:
        raise_value_error(f"Число {count} вне диапазона 1..10^5")


def validate_rgb(rgb: List[int]) -> List[int]:
    if len(rgb) != 3:
        raise_value_error(f"Ожидалось три числа, а получено: '{",".join(map(str, rgb))}'")
    for count in rgb:
        validate_count(count)
    return rgb


def get_rgb_from_input() -> List[int]:
    data = input("Количество шариков (red, green, blue): ").strip()
    rgb = list(map(int, data.split(",")))
    return validate_rgb(rgb)


def get_rgb_from_argv(argv: List[str]) -> Optional[List[int]]:
    return get_args(argv, "/rgb", mapper=int, validator=validate_count)

@lru_cache(maxsize=None)
def get_count(r, g, b, last: Color = None):
    if r < 0 or g < 0 or b < 0:
        return 0
    if r == 0 and g == 0 and b == 0:
        return 1
    res = 0
    if last != Color.RED and r > 0:
        res += get_count(r - 1, g, b, Color.RED) % MOD
    if last != Color.GREEN and g > 0:
        res += get_count(r, g - 1, b, Color.GREEN) % MOD
    if last != Color.BLUE and b > 0:
        res += get_count(r, g, b - 1, Color.BLUE) % MOD
    return res % MOD


def main() -> None:
    try:
        rgb = get_rgb_from_argv(sys.argv) or get_rgb_from_input()
        count = get_count(*rgb)
        print(count)
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
