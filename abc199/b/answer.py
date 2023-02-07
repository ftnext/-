if __name__ == "__main__":
    n = int(input())
    as_ = map(int, input().split())
    bs = map(int, input().split())

    a_max = max(as_)
    b_min = min(bs)

    if a_max <= b_min:
        print(b_min - a_max + 1)
    else:
        print(0)
