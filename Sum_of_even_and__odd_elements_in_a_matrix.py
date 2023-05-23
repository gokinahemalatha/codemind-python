def calculate_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    even_sum = 0
    odd_sum = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] % 2 == 0:
                even_sum += matrix[i][j]
            else:
                odd_sum += matrix[i][j]
    
    return even_sum, odd_sum

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

even_sum, odd_sum = calculate_sum(matrix)

print(even_sum, odd_sum)