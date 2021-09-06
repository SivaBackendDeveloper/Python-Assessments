#3. Write a program to read a file stream


file = open('sample.txt', 'r', encoding="utf-8")
# reading first line data from the file using readline() method
data = file.readline()
# printing the data
print(data)
# closing the file
file.close()
