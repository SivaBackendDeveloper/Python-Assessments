#11. Write a program to find the common values between two arrays

import numpy as np

s=np.array([1,2,3,4])
c=np.array([1,8,6,7,3])
# intersect1d function is used to finding the same elements in two arrays
l=np.intersect1d(s,c)
print(l)