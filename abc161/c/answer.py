N, K = map(int, input().split())
while True:
    if N % K == 0:
        print(0)
        break
    if abs(N - K) >= N:
        print(N)
        break
    N = N % K
