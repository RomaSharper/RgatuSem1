from typing import List
from functools import lru_cache
from color import Color

MOD = 998244353


def get_rgb() -> List[int]:
    data = input()
    rgb = list(map(int, data.split()))
    if len(rgb) != 3:
        raise ValueError(f"Ожидалось три числа, а получено: \"{data}\"")
    if any(color < 1 or color > 10**5 for color in rgb):
        raise ValueError(f"Все числа должны быть > 1 и < 10**5")
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


if __name__ == '__main__':
    try:
        user_rgb = get_rgb()
        count = get_count(*user_rgb)
        print(count)
    except ValueError as ve:
        print(ve)
