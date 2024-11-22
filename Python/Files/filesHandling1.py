

# "a" Append    Open file for appending values and create file if not exists
# "r" Read      Open file for read give error if file not exists
# "w" Write     Open file for writing create if file not exists
# "x" Create    create file give error if file exists 

# "a+"          Open file for appending values and reading and create file if not exists
# "r+"          Open file for read and write give error if file not exists
# "w+"          Open file for writing and read and create if file not exists
# "x+"          Create and read file give error if file exists

# Absloute Pass
# Relative Pass


import os

print()
print()
print()

print(os.getcwd()) # 1

print()

print(os.path.dirname(os.path.abspath(__file__))) # 2

#print((os.path.abspath(__file__)))

print()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd()) # 3

print()


f = open("H:\\Python\\nfiles\\osama.txt")







