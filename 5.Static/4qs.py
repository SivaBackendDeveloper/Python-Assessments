#Define a static variable and change within the class

class student:
    dept = 'Information technology'  #  static variable

    def __init__(self, name, rollnumber):
        self.name = name  # instance variable
        self.rollnumber = rollnumber  # instance variable

# Define the objects of student class
st1 = student('Siva', '318')

print(st1.dept)
print(st1.name)
print(st1.rollnumber)

# Access class variable using the class name
print(student.dept)  # print the department

# change the department of static variable with in the class
student.dept = 'Mechanical'
print(student.dept)

