myRange = range(1, 100)

#for number in myRange :
    #print(number)


mySkills = {
    "Html" : "90%",
    "Css" : "60%",
    "PHP" : "70%",
    "JS" : "80%",
    "Python" : "40%",
    "MySQL" : "30%"
}    



#print(mySkills["JS"])
#print(mySkills.get("Python"))



for skill in mySkills :
    
    print(f"My Progress In Lang {skill} Is : {mySkills.get(skill)}")

    