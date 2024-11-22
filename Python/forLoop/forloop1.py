myNumber = [1,2,3,4,5,6,7,8,9]

for number in myNumber :
    #print(number * 17)

    if number % 2 == 0 :

        print(f"The Number {number} Is Even.")

    elif number % 2 != 0 :
        print(f"The Number {number} Is Odd.")


else :
    print("Loop Is Finished")            


myName = "Osama"
for letter in myName :
    print(f" [ {letter.upper()} ] ")