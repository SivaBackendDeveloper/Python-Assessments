#17. Write a method to verify if the array contains two specified elements(12,23)
import array


def sp_ele_array(x,y):
    arr=array.array('i',[12,58,59,48,23])
    if x in arr and y in arr :
        print(x,y,"inside elements of array")
    else:
        print("sorry element not find in array")

sp_ele_array(12,23)