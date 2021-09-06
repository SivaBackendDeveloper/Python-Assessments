#2. Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.
#Also, Access the PROTECTED fields and methods from child class located in a different package
#Access the PROTECTED fields and methods from any class in different package

#base class
class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None
    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)

# derived class
class details(Student):
    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
    # public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)
        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = details("SIVA", 318, "MECHANICAL")

# calling public member functions of the class
obj.displayDetails()