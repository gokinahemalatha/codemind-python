def printString(n):
    arr = [0] * 10000
    i = 0
    while (n > 0):
        arr[i] = n % 26
        n = int(n // 26)
        i += 1
    for j in range(0, i - 1):
        if (arr[j] <= 0):
            arr[j] += 26
            arr[j + 1] = arr[j + 1] - 1
 
    for j in range(i, -1, -1):
        if (arr[j] > 0):
            print(chr(ord('A') +
                  (arr[j] - 1)), end = "");
 
    print();
n=int(input())
printString(n)