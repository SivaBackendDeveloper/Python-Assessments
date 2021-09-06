#. Write a program with multiple catch blocks

a,b=1,0
try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError: #catch blocks
          print("You added values of incompatible types")
except ZeroDivisionError: # catch blocks
          print("You divided by 0")