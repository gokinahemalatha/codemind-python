N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_of_elements = 0
for i in range(N):
    for j in range(M):
        sum_of_elements += matrix[i][j]

print(sum_of_elements)