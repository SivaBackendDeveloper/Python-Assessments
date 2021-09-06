#1. Write a class with a default constructor, one argument constructor and two argument constructors.
# Instantiate the class to call all the constructors of that class from a main class


class Employee:
    def __init__(self): # default constructor
        print("HI")
    # i am using  Nested class
    class Name:
        def __init__(self, name):  # one argument constructor
            self.name = name


    class id_Loction:
        def __init__(self, id, location):  # two argument constructor
            self.id = id
            self.location = location



# printing  default constructor
emp=Employee()
# Printing   one argument constructor with the help of main class
n=emp.Name("siva")
print(f'Employee name ={n.name}')
# Printing   two argument constructor with the help of main class
il=emp.id_Loction(101,"HYD")
print(f'Employee id ={il.id} and location is {il.location}')