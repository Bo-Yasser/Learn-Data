myTuple = ("Html","CSS","JS")




mySkills = {
    "PHP" : "50", 
    "Python": "80",
    "Go" : "30"
}



def show_skills(name, *skills, **skillsWithProgress) :

    print(f"Hello {name}. \nSkills Without Progress Is : ")

    for skill in skills :

        print(f"- {skill}")
    
    print("Skills With Progress : ") 

    for skill_key, skill_value in skillsWithProgress.items() :

        print(f"- {skill_key} => {skill_value}%")





show_skills("Osama",*myTuple,**mySkills)    

print("-"* 20)

show_skills("Mohamed", "Python", "JAVA" , JS = "80" )