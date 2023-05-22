n = int(input())
array = list(map(int, input().split()))
last_even_index = None

for i in range(n - 1, -1, -1):
    if array[i] % 2 == 0:
        last_even_index = i
        break


print(last_even_index)
