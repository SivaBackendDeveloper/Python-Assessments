#18. Write a program to remove the duplicate elements and return the new array

def remove_duplicate_newarray(arr, n):
    # Return, if array is
    # empty or contains
    # a single element
    if n == 0 or n == 1:
        return n

    temp = list(range(n))

    # Start traversing elements
    j = 0
    for i in range(0, n - 1):

        # If current element is
        # not equal to next
        # element then store that
        # current element
        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j += 1

    # Store the last element
    # as whether it is unique
    # or repeated, it hasn't
    # stored previously
    temp[j] = arr[n - 1]
    j += 1

    # Modify original array
    for i in range(0, j):
        arr[i] = temp[i]

    return j


# Driver code
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print("before =",arr)
n = len(arr)

# removeDuplicates() returns
# new size of array.
n = remove_duplicate_newarray(arr, n)

# Print updated array
print("After : ")
for i in range(n):
    print("  %d" % (arr[i]), end=" ")


