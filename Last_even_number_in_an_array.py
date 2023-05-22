n = int(input())
input_array = list(map(int, input().split()))

last_even = None  # Initialize the variable to None
for num in input_array:
    if num % 2 == 0:  # Check if the number is even
        last_even = num  # Update the variable with the current even number

print( last_even)