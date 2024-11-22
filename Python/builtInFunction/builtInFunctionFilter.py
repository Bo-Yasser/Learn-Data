
# EX 1

def checkNumber(num) :

   return num > 10


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]    


myResult = filter(checkNumber, myNumbers)


# for n in myResult :

    #print(n)



print("#"* 50)


# EX 2



def checkName(name) :

    return name.startswith("O")




myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnData = filter(checkName, myTexts)


#for person in myReturnData :

    #print(person)



print("#"* 50)


# EX 3    


myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

myReturnedNames = filter(lambda name: name.startswith("A") , myNames)


for name in myReturnedNames :

    print(name)









