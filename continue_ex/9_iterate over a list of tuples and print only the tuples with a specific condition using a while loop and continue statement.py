#iterate over a list of tuples and print only the tuples with a specific condition using a while loop and continue statement.
tuple_list = [(1, 'apple'), (2, 'banana'), (3, 'melon'), (4, 'watermelon'), (5, 'strawberry')]
target_condition = 'melon'
i = 0
while i < len(tuple_list):
        if target_condition not in tuple_list[i][1]:
            i += 1
            continue
        print(tuple_list[i])
        i += 1

