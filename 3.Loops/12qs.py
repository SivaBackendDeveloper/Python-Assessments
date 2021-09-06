#Print gender (Male/Female) program according to given M/F using switch

def switch(arg):
    switcher={
        "M":"Male",
        "m": "Male",
        "F":"Female",
        "f": "Female",
         }
    return switcher.get(arg,"nothing")

if __name__=="__main__":
    arg=input("enter a letter =")
    print(switch(arg))
