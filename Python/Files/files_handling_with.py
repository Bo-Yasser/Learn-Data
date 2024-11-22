import os 
# print(os.path.abspath(__file__))


# file = open(r"h:\Python\Files\with.csv", "a+")

with open(r"h:\Python\Files\with.csv", "a+") as file :
    file.write("With Function")
    print(file.read())
    