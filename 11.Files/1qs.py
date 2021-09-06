#1. Write a program to read text

# opening a file in 'r'
file = open('sample.txt', 'r')
# reading data from the file using read() method
data = file.read()
# printing the data
print(data)
# closing the file
file.close()

