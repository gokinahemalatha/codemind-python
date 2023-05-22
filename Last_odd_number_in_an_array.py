n = int(input())
input_array = list(map(int, input().split()))

last_odd = None  
for num in input_array:
    if num % 2 != 0:  
        last_odd = num 

print(last_odd)