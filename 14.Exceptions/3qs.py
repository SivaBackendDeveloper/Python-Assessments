# . Write a method which throws exception, Call that method in main class without try block

class class_method:
    def __init__(self):
        print("this is main class")
    # Method
    def method(self):
        a=20
        b="siva"
        print(a+b) # exception condition


obj=class_method()
obj.method() # Calling that method in main class without try block
