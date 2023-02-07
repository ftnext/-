N, M = map(int, input().split())
votes = list(map(int, input().split()))
min_votes = sum(votes) * 1.0 / (4*M)
votes_greater_than_min = list(filter(lambda x: x >= min_votes, votes))
if len(votes_greater_than_min) >= M:
    print('Yes')
else:
    print('No')
