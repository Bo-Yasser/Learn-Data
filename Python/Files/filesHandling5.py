
# "a+"          Open file for appending values and reading and create file if not exists
# "r+"          Open file for read and write give error if file not exists
# "w+"          Open file for writing and read and create if file not exists
# "x+"          Create and read file give error if file exists  



import os

print(os.path.abspath(__file__))

file = open(r"H:\Python\text.txt", "r+")

print(file.readable())

file.write("Mohamed")
file.write(" Yaser")

