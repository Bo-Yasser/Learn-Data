mySkills = {
    "Html" : "80%",
    "CSS" : "90%",
    "JS" : "70%",
    "PHP" : "80%"
}



#for skill_keys, skill_value  in mySkills.items() :
    
    #print(f"{skill_keys} => {skill_value}")



myUltimateSkills = {
    "Html" : {
        "Main" : "80%",
        "Pugjs" : "80%"
    },
    "CSS" : {
        "Main" : "90%",
        "Sass" : "70%"
    }
}

for main_key, main_value in myUltimateSkills.items() :
    
    print(f"\"{main_key.upper()}\" Progress Is : ")


    for child_key, child_value in main_value.items() : 

        print(f"- {child_key.upper()} : {child_value}")




