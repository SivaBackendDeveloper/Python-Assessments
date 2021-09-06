#2. Call the constructors(both default and argument constructors) of super class from a child class

"""

When you define another constructor in your class, you do not get the "usual" default constructor (public and without arguments) anymore.
 Of course, when creating an object instance using new you have to choose which one to call (you cannot have both)
"""

class Person:

    def __init__(self): # Default constructor
        print("HI")

    def __init__(self, n): # argument constructor
        self.name = n


class Employee(Person):

    def __init__(self, i, n):

        #super().__init__()
        super().__init__(n)  # same as Person.__init__(self, n)
        self.id = i


emp = Employee(99, 'SIVA')
print(f'Employee ID is {emp.id} and Name is {emp.name}')
