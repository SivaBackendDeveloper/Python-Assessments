#12. Write a method to remove duplicate elements from an array

import numpy as np

def remove_duplicates(x):
    arr = np.array(x)
    lst = []
    for i in arr:
        if i not in lst:
            lst.append(i)

    print(lst)

x=["a", "b", "b", "c", "a"]
remove_duplicates(x)
