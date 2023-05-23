N, M = map(int, input().split())

matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

max_row_sum = 0
for i in range(N):
    row_sum = sum(matrixA[i])
    if row_sum > max_row_sum:
        max_row_sum = row_sum
print(max_row_sum)