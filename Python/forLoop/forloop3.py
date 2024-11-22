peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ["Html", "Css", "JS"]

#for name in peoples :
    
    #print(f"{name} Skills Is : ")

    #for skill in skills :

        #print(f"- {skill}")


peoples2 = {
    "Osama" : {
        "Html" : "70%",
        "Css" : "80%",
        "JS" : "70%"
    },
    "Ahmed" : {
        "Html" : "90%",
        "Css" : "80%",
        "JS" : "90%"
    },
    "Sayed" : {
        "Html" : "70%",
        "Css" : "60%",
        "JS" : "90%"
    }
} 


#print(peoples2["Osama"])
#print(peoples2["Ahmed"])
#print(peoples2["Sayed"])

#print(peoples2["Osama"]["Css"])
#print(peoples2["Ahmed"]["Css"])
#print(peoples2["Sayed"]["Css"])


for name in peoples2 :
    print(f"Skills And Progress For {name} Is : ")

    for skill in peoples2[name] :
        
        print(f"{skill.upper()} => {peoples2[name][skill]}")
        


