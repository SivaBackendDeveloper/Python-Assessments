#6. Write a function to copy an array to another array


# importing the module
import array

from numpy import *

def copy_array(x):
    # creating the first array
    arr1 = array(x)
    # shallow copy arr1 in arr2 using view()
    arr2 = arr1.copy()
    # making a change in arr1
    arr1[1] = 7
    # displaying the arrays
    print(arr1)
    print(arr2)

x=[2, 6, 9, 4]
copy_array(x)