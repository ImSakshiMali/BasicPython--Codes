#find the sum of all numbers between 1 and 100, excluding the multiples of 5 using a for loop and continue statement.
total_sum = 0
for num in range(1, 101):
    if num % 5 == 0:
        continue
    total_sum += num
print("The sum of numbers from 1 to 100 (excluding multiples of 5) is:", total_sum)