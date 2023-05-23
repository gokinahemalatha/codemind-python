def sum_non_boundary(matrixA):
    rows = len(matrixA)
    cols = len(matrixA[0])
    total_sum = 0

    for i in range(rows):
        for j in range(cols):
            if i != 0 and i != rows - 1 and j != 0 and j != cols - 1:
                total_sum += matrixA[i][j]

    return total_sum
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

result = sum_non_boundary(matrixA)


print(result)