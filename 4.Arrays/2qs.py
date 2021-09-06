#2. Write a function to calculate the average value of an array of integers

import array as arr

a = arr.array('i', [1, 2, 3])
s=0
for i in a:
    s+=i

print("average value of an array =",s)
