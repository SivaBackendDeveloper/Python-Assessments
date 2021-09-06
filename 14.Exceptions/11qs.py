#11. Write a program to generate IOException

import sys
def readFile():
    try:
        f = open ( "xyz.txt", 'r' )
    except IOError as e:
        print (e)
readFile()