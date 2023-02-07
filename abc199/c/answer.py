import sys


def swap_letter(string, i1, i2):
    """Ti = 1のクエリを表す関数

    i1, i2は文字列のインデックス

    >>> swap_letter("FLIP", 0, 1)
    'LFIP'
    >>> swap_letter("FLIP", 3, 1)
    'FPIL'
    >>> # swap_letter("FLIP", 2, 2)  # Ai < Bi なので考えない
    """
    # 前提: i1 != i2
    if i1 > i2:
        i1, i2 = i2, i1
    # i1 < i2
    # + から変えてみたが効果なし
    return "".join(
        (
            string[:i1],
            string[i2],
            string[i1 + 1 : i2],
            string[i1],
            string[i2 + 1 :],
        )
    )


def swap_half(string, n):
    """Ti = 2のクエリを表す関数

    仮定: len(string) == 2n

    >>> swap_half("FLIP", 2)
    'IPFL'
    """
    return string[n:] + string[:n]


def half_slide(map_, half_length):
    """
    >>> map_ = {1: 1, 2: 2, 3: 3, 4: 4}
    >>> half_slide(map_, 2)
    {1: 3, 2: 4, 3: 1, 4: 2}
    """
    full_length = 2 * half_length
    return {
        k: (v + half_length) % full_length
        if (v + half_length) > full_length
        else v + half_length
        for k, v in map_.items()
    }


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    s = input().rstrip()  # len(s) == 2n
    q = int(input())
    ts, as_, bs = [], [], []
    for i in range(1, q + 1):
        t, a, b = list(map(int, input().rstrip().split()))
        ts.append(t)
        as_.append(a)
        bs.append(b)

    s_length = 2 * n
    indices_map = {i: i for i in range(1, s_length + 1)}
    for t, a, b in zip(ts, as_, bs):
        if t == 1:
            indices_map[a], indices_map[b] = indices_map[b], indices_map[a]
        else:
            indices_map = {
                k: (v + n) % s_length if (v + n) > s_length else v + n
                for k, v in indices_map.item()
            }
    print(s)
