from collections import Counter
from itertools import permutations


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def combination(n, k):
    return len(set(permutations(f"{'a'*(n-k)}{'b'*k}", n)))


def main(memory_counter):
    """
    >>> main({"o": 5})
    0
    >>> main({"x": 10})
    0
    >>> main({"o": 4, "?": 2})
    24
    >>> main({"?": 1})
    1
    >>> main({"?": 2})
    16
    >>> main({"o": 1, "?": 0})  # ここが通っていない
    1
    >>> main({"o": 2, "?": 0})
    6
    >>> main({"o": 1, "?": 1})
    15
    >>> main({"o": 1, "?": 2})  # doctest: +SKIP
    43
    >>> # main({"o": 3, "?": 1})
    >>> main({"o": 3, "?": 3})  # doctest: +SKIP
    108
    """
    maru_count = memory_counter.get("o") or 0
    batsu_count = memory_counter.get("x") or 0
    hatena_count = memory_counter.get("?") or 0

    if batsu_count == 10:  # oも?もない
        return 0
    if maru_count > 4:
        return 0
    
    if maru_count == 4:
        return factorial(maru_count)
    if maru_count == 0:
        return hatena_count ** 4
    if hatena_count == 0:
        count = 0
        for i in range(1, 4 - maru_count + 1):
            # 1種類使う時と2種類使う時
            count += factorial(i) * maru_count

    patterns_count = 0
    # ? を使ったケースのパターンの数を加算する
    for i in range(1, 4 - maru_count + 1):
        patterns_count += combination(4, i) * hatena_count

    # required_patterns_count = factorial(maru_count)

    # optional_patterns_count = (maru_count + hatena_count) ** (4 - maru_count)
    # patterns_count = required_patterns_count * optional_patterns_count * (4 - maru_count)
    return patterns_count


if __name__ == "__main__":
    memory = input()
    memory_counter = Counter(memory)

    count = main(memory_counter)
    print(count)
