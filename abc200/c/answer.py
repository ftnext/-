from __future__ import annotations

from collections import defaultdict
from functools import lru_cache

# import sys
# sys.setrecursionlimit(200001)  # N <= 2e05


@lru_cache
def pair_count(number: int) -> int:
    """
    >>> pair_count(1)
    0
    >>> pair_count(2)
    1
    >>> pair_count(3)
    3
    >>> pair_count(5)
    10
    """
    return number * (number - 1) // 2
    # if number == 1:
    #     return 0
    # return (number - 1) + pair_count(number - 1)  # なぜ再帰にしていたのか


def count_amari_200(values: list[int]) -> int:
    """
    >>> count_amari_200([2, 20])
    1
    >>> count_amari_200([1, 2, 1, 5])
    3
    """
    length = len(values)
    even_length = sum(v % 2 == 0 for v in values)
    odd_length = length - even_length
    count = 0
    if even_length:
        count += pair_count(even_length)
    if odd_length:
        count += pair_count(odd_length)
    return count


def main(As: list[str]) -> int:
    """
    >>> main(["001", "002", "003", "004", "005"])
    0
    >>> main(["123", "223", "123", "523"])
    3
    >>> main(["003", "603", "203"])
    3
    >>> main(["2000", "200"])
    1
    """
    same_last_2digits = defaultdict(list)
    for a in As:
        same_last_2digits[a[-2:]].append(int(a[:-2]))

    count = 0
    for value_list in same_last_2digits.values():
        count += count_amari_200(value_list)
    return count


if __name__ == "__main__":
    N = int(input())
    As = [i.zfill(3) for i in input().split()]

    print(main(As))
