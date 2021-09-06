#4. Write a function to test if array contains a specific value

import array as arr

def specific_value(n):
    # taking list
    lst = [1,8,5,22,85,318]
    a=arr.array('i',lst)
    for i in a:
        if n == i:  # this condition is checking 10.5 in the lst
            print(n, "it is inside value")
            break
    else:
        print(n, "is not in the value")

specific_value(22)
specific_value(15)