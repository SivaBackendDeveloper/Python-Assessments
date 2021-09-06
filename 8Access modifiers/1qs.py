#1. Create a class with PRIVATE fields, private method and a main method. Print the fields in main method.
# Call the private method in main method.
#Create a sub class and try to access the private fields and methods from sub class.

class main:
   # main method
    def fun(self):
        print("Public method")
    # private method
    def __fun(self):
        print("Private method")
# Creating a derived class
class sub(main):
    def __init__(self):
        # Calling constructor of
        # Base class
        main.__init__(self)
    def call_public(self):
        # Calling main method of base class
        print("\nInside derived class")
        self.fun()
    def call_private(self):
        # Calling private method of base class
        self.__fun()
# Driver code
obj1 = main()
# Calling public method
obj1.fun()
obj2 = sub()
obj2.call_public()
