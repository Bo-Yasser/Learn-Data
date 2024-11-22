mySKills = {
    "Html" : "70%",
    "CSS" : "50%", 
    "JS" : "40%",
    "Python": "80%",
    "Go" : "30%"
}

def show_skills(**skills) : 
    
    print(type(skills))
    
    for skill, value in skills.items() :
       print(f"{skill} => {value}")

       

show_skills(Html = "70%", CSS = "50%", JS = "40%", Python = "80%", Go = "30%")

print("-" * 20)

show_skills(**mySKills)
