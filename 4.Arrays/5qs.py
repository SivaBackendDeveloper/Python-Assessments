#5. Write a function to remove a specific element from an array

# initializes array with signed integers
import array

def remove_sp_element(x):
    arr = array.array('i', [1, 2, 3, 1, 5])

    # printing original array
    print("The new created array is : ", end="")
    for i in range(0, 5):
        print(arr[i], end=" ")

    print("\r")

    # using pop() to remove element by the index position
    print("The popped element is : ", end="")
    print(arr.pop(x)) # By using of pop () ,remove() fun also we can use

    # printing array after popping
    print("The array after popping is : ", end="")
    for i in range(0, 4):
        print(arr[i], end=" ")

    print("\r")

remove_sp_element(2)