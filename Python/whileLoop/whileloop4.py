tries = 4

mainPassword = "Osama@123"

inputPassword = input("Write Your Password : ")

while inputPassword != mainPassword : 

    tries -= 1 

    print(f"Wrong Password {"Last" if tries == 0 else tries} Chance Left.")

    inputPassword = input("Write Your Password : ")

    if tries == 0 :
        print("All Tries Has Finished")

        break

else:

    print("Correct Password")
