import sys


# print(sys.path)
# sys.path.append(r"H:\Python")
# print(sys.path)


# print(sys.version)
# print(sys.platform)

# sys.exit()

# if len(sys.argv) == 2:   # argv back [] and 0 index is name of file 

#     print(f"Hello {sys.argv[1]}")

# else:
#     print("Hello World")    


# print(type(sys.argv))
# print(dir(sys.argv))

for i in sys.argv[1:]:
    print(i)