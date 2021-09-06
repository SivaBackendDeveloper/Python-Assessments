#6. Write a program to check whether a file is having read access and write access permissions

import os

print(os.access("sample.txt",os.R_OK))# checking read access

print(os.access("sample.txt",os.W_OK))# checking write access


