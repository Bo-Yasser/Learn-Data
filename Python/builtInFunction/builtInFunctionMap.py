
# def formatText(text):

    # return f"- {text.strip().capitalize()} -"


#myText = [" OSama ", "AHMED", "  sAYed  "]

# myFormatedData = map(formatText, myText)

# print(myFormatedData)


#for name in list(map(formatText, myText)) :

    #print(name)










myText = [" OSama ", "AHMED", "  sAYed  "]

# myFormatedData = map(formatText, myText)

# print(myFormatedData)


for name in list(map(lambda text : f"- {text.strip().capitalize()} -", myText)):

    print(name)




