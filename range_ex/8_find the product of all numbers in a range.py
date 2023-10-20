#find the product of all numbers in a range.
def product_range(start, end):
    product = 1
    for number in range(start, end + 1):
        product *= number
    return product
result = product_range(1, 5)
print(result)





