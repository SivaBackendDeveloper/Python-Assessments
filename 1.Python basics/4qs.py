#Define the local and Global variables with the same name and print both variables and understand the scope of the variables ?

a=10

def local():
    a=100
    print("local variable a =",a)

local()
print("global variable a=",a)

