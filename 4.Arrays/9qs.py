#9. Write a function to reverse an array of integer values

from numpy import *

def reverse(x):
    a = array(x)
    # -1 starts with end value in array
    print(a[::-1])

s=[1,2,3,4,5,6,7,8,9]
reverse(s)