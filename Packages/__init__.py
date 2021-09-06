# Create a __init__.py for adding all packages
# Import the respective packages
# Call each class by creating an object to it
from pythonProject.pyassissments.function import *
from pythonProject.pyassissments.greet import sayhello
from pythonProject.pyassissments.Packages.qs import Color

#functions are importing from other py files

print(sayhello("siva"))
print(sum(10,20))
print(avg(20,50))
print(power(10,3))

# create Color class object
outer = Color()

# method calling
outer.show()

# create a Lightgreen
# inner class object
g = outer.lg

# inner class method calling
g.display()
