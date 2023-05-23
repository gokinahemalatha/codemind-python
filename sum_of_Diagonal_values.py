def sum_diagonal_values(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    diagonal_sum = 0

    for i in range(rows):
        for j in range(cols):
            if i == j or i + j == rows - 1: 
                diagonal_sum += matrix[i][j]

    return diagonal_sum

N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

result = sum_diagonal_values(matrixA)
print(result)