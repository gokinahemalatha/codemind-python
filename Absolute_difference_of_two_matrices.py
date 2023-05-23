
N = int(input())

matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)


matrixB = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixB.append(row)

diffMatrix = []

for i in range(N):
    diffRow = []
    for j in range(N):
        diff = abs(matrixA[i][j] - matrixB[i][j])
        diffRow.append(diff)
    diffMatrix.append(diffRow)


for row in diffMatrix:
    print(' '.join(map(str, row)))