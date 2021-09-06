#Define a static variable and change within the instance

class student:
    dept = 'Information technology'  #  class variable

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

# change the department of particular instance
st1.dept = 'Mechanical'
print(st1.dept)



