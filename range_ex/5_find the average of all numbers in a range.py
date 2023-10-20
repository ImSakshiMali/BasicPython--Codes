#find the average of all numbers in a range.
start = 1
end = 20
sum = sum(range(start,end))
count = end - start
if count > 0:
    avg = sum / count
else:
    avg = 0
print("Average of all numbers in range :",avg)