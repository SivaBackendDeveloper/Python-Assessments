#8. Write a function to find the minimum and maximum value of an array

import array
from numpy import *
def max_min(x):
    arr1 = array(x)
    # using max () function
    print("maximum in array =", max(arr1))
    # using max () function
    print("minimum in array =", min(arr1))


x=[2, 6, 9, 4]
max_min(x)