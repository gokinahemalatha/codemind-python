N, M = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

max_col_sum = 0
for j in range(M):
    col_sum = sum(A[i][j] for i in range(N))
    if col_sum > max_col_sum:
        max_col_sum = col_sum
print(max_col_sum)