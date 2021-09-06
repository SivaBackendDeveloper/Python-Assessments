"""
1. Create a program to create two class.
   1.1. Create a constructor and a method for each class
   1.2. Create a __init__.py for adding all packages
   1.3. Import the respective packages
   1.4. Call each class by creating an object to it
   1.5. Create a program by all the above
"""

#Create a program to create two class.
#reate a constructor and a method for each class
class Color:

    # constructor method
    def __init__(self):
        # object attributes
        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print("Name:", self.name)

    # create Lightgreen class
    class Lightgreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)




