# __name__ is built in veriable in python and his value == __main__

# File One

print("Print From File One")



if True:
    print("True")

else:
    print("False")


if __name__ == "__main__":
    print("File One Is Running Directly")
    
    def hello():

        print("Print Function From File One")
        
else:
    print("You Are NOT Running File One Directly")     



hello()    