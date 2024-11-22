uName = "Osama"
isStudent = "No"
uCountry = "Qatar"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":
    
    if isStudent == "Yes":
        print(f"Hello {uName} Because You Are Form {uCountry} And Student")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 90}")
    elif isStudent == "No" : 
        print(f"Hello {uName} Because You Are Form {uCountry} ")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 80}")    


elif uCountry == "Kuwait" or uCountry == "Bahrain":
    print(f"Hello {uName} Because You Are Form {uCountry} ")
    print(f"The Course \"{cName}\" Price Is : {cPrice - 50}$ ") 

else:
    print(f"Hello {uName} Because You Are Form {uCountry} ")
    print(f"The Course \"{cName}\" Price Is : {cPrice - 30}$ ")







