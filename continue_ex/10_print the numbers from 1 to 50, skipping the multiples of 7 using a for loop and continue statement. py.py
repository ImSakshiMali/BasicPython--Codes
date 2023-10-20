#print the numbers from 1 to 50, skipping the multiples of 7 using a for loop and continue statement.
for i in range(1, 51):
    if i % 7 == 0:
        continue
    print(i)
