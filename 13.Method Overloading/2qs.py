#2. Write two methods with the same name but different number of parameters of different  data type and call the methods


def method(a,b):
    c=a+b
    print(c)

def method(a,b,c):
    s=a+b+c
    print(s)

method("hi","hello","world")
method(10,20,10)