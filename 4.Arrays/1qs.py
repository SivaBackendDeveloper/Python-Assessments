# Write a function to add integer values of an array

import array as arr

a=int(input("enter array size ="))
l=[]
k=1
while k<=a:
    n=int(input("enter a number ="))
    l.append(n)
    k+=1
ar=arr.array('i',l)
for i in range(a):
    print(ar[i],end=" ")


