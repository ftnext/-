A = list(map(int, input().split()))
A.sort()

if A[1] - A[0] == A[2] - A[1]:
    print("Yes")
else:
    print("No")

"""Wrong answer

A = list(map(int, input().split()))
diff21 = abs(A[2] - A[1])
diff10 = abs(A[1] - A[0])
diff20 = abs(A[2] - A[0])

if len(set([diff21, diff10, diff20])) <= 2:
    print("Yes")
else:
    print("No")
"""
