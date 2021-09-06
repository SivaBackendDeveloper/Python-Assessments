#5. Write a program to read a file a just to a particular index using seek()


file = open('sample.txt', 'r')

file.seek(1) #seek is using for starting index to read

print(file.read())
file.close()
