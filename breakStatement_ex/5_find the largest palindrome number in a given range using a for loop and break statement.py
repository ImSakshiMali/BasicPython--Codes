#find the largest palindrome number in a given range using a for loop and break statement.
def is_palindrome(num):
    return str(num) == str(num)[::-1]
largest_palindrome = 0
for num in range(100, 0, -1):
    if is_palindrome(num):
        largest_palindrome = num
        break
print(f"The largest palindrome number in the given range is {largest_palindrome}")