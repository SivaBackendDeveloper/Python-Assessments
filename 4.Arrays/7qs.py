#7. Write a function to insert an element at a specific position in the array

import array as arr

def insert_element(s,c):
    # creating an array with integer type
    a = arr.array('i', [1, 2, 3])

    # printing original array
    print("The new created array is : ", end=" ")
    for i in range(0, 3):
        print(a[i], end=" ")
    print()

    # adding intiger value array using
    # insert() function
    a.insert(s, c)
    #s= Index reference where we put element
    #c= Element

    print("Array after insertion : ", end=" ")
    for i in (a):
        print(i, end=" ")
    print()

insert_element(1,20)