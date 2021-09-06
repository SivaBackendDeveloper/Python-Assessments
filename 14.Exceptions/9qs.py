#9. Write a program to generate FileNotFoundException

import sys

try:
    file=open("d:/wwwwwww.txt","r")

except FileNotFoundError:
    print("sorry dude file not found ")
    sys.exit()

# in file handling system open and close function are important

a=file.read()
print(a)
file.close()