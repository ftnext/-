""" Solve https://atcoder.jp/contests/abc198/tasks/abc198_b """


def is_already_kaibun(digits: str) -> bool:
    """
    >>> is_already_kaibun("777")
    True
    >>> is_already_kaibun("1210")
    False
    """
    reversed = digits[::-1]
    return digits == reversed


def main(N: str) -> None:
    # 右（末尾）にある全ての0をとって回文なら、先頭に0を0個以上付けて回文にできる
    zero_striped = N.rstrip("0")
    if is_already_kaibun(zero_striped):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    N = input()
    main(N)
