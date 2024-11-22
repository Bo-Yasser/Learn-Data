
#import os 

#print(os.path.abspath(__file__))

myFile = open(r"h:\Python\Files\osama.txt", "r")

# 1
'''print(myFile)
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)'''

# 2
'''print(myFile.read())
print(myFile.read(5))'''

# 3
'''print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())
'''

# 4
'''print(myFile.readlines())
print(myFile.readlines(50))
print(type(myFile.readlines()))
'''

for line in myFile :

    print(line)

    if line.startswith("07") :

        break 


myFile.close()    