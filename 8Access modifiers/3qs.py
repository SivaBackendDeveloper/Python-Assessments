#3. Create a class with PUBLIC fields and methods.
#Access the public methods and fields from any class in the same package or different package.
class person:
    # constructor
    def __init__(self, name, age):
        # public data mambers
        self.Name = name
        self.Age = age
    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.Age)

# creating object of the class
obj = person()
# accessing public data member
print("Name: ", obj.Name)
# calling public member function of the class
obj.displayAge()