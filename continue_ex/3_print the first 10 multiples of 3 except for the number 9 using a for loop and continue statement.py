#print the first 10 multiples of 3 except for the num 9 using a for loop and continue statement.
count = 0
for number in range(1, 31):
    if number % 3 != 0 or number == 9:
        continue
    print(number)
    count += 1
    if count == 10:
        break