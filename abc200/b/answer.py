def add_200(digits: str) -> str:
    """
    >>> add_200("7")
    '7200'
    >>> add_200("1234")
    '1234200'
    """
    return f"{digits}200"


def operate(digits: str) -> str:
    """
    >>> operate("7")
    '7200'
    >>> operate("7200")
    '36'
    >>> operate("7100")
    '7100200'
    """
    if not digits.endswith("00"):
        return add_200(digits)
    if int(digits[-3]) % 2 == 0:
        return str(int(digits[:-2]) // 2)
    return add_200(digits)


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    value = str(N)
    for _ in range(K):
        value = operate(value)
    print(value)
