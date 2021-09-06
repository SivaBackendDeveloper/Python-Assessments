#2. Write a program to write text to .txt file using InputStream

# opening a file in 'w'
file = open('sample.txt', 'w')
# writing data using the write() method
file.write("I am a Python programmer.\nI am happy.")
# closing the file
file.close()