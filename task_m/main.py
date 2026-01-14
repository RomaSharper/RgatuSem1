from typing import List
from functools import lru_cache
from color import Color

MOD = 998244353


def to_number(num: str) -> int:
    num = num.strip()
    if not num.removeprefix("-").isnumeric():
        raise ValueError(f"Ожидалось число, а получено: '{num}'")
    num = int(num)
    if num < 1 or num > 10 ** 5:
        raise ValueError(f"Число должно быть в диапазоне 1..10^5, а получено: {num}")
    return num


def get_rgb() -> List[int]:
    data = input().strip()
    rgb = list(map(to_number, data.split(" ")))
    length = len(rgb)
    if length != 3:
        raise ValueError(f"Ожидалось 3 числа, а получено {length}")
    return rgb


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
        print("Ввод:")
        user_rgb = get_rgb()
        print("\nВывод:")
        print(get_count(*user_rgb))
    except ValueError as ve:
        print("\nОшибка:")
        print(ve)


if __name__ == '__main__':
    main()
