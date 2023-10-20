#print all even numbers in a given range.
start = 1
end = 10 #not included 10
for e in range(start,end+1): # end+1 means include 10 i.e. the last number
    if e%2 == 0:
        print(e)