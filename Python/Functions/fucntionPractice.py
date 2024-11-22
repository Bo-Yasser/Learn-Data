# 1
'''
# add, subtract, multiply

def calculate(num1, num2, operator= "add"):

    operator = operator.lower()

    if operator in ["add", "a"]:

        return num1 + num2

    elif operator in ["subtract", "s"]:

        return num1 - num2    

    elif operator in ["multiply", "m"]:

        return num1 * num2


    else:

        return "Operator Is Not Valid"    



print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30
print("#" * 50)


print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10
print("#" * 50)


print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200
'''



# 2

'''
def addition(*num):

    sum = 0

    for n in num :

        if n == 10 :
            continue

        if n == 5 :
            sum -= 5

        else:

            sum += n  

    return sum


print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
'''




# 3


'''
def show_skills(name, *skills) :

    if bool(skills) :

        print(f"Hello {name} Your Skills Is: ")

        for s in skills :

            print(f"- {s}")


    else:
        print(f"Hello {name} You Have No Skills To Show")



show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")
'''





# 4

'''
def say_hello(name= "Unknown", age= "Unknown", country= "Unknown"):


    return f"Hello {name} Your Age Is {age} And You Live In {country}"


print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
'''




# 5


'''
def get_score(**score) :

    for key, value in score.items() :

        print(f"{key} => {value}")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)
'''




# 6

'''
def get_people_scores(name="", **score):

    if len(score) > 0 :
        
        if bool(name) :

            print(f"Hello {name} This Is Your Score Table:")

        for s in score :

            print(f"{s} => {score[s]}")   
    else: 

        print(f"Hello {name} You Have No Scores To Show")

#get_people_scores("Osama", Math=90, Science=80, Language=70)  
#get_people_scores("Mahmoud", Logic=70, Problems=60)    
#get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")
'''






# 7

scores_list = {
    "Math" : 90,
    "Science" : 80,
    "Language" : 70
} 


'''
def get_the_scores(name="", **dict):

    if len(dict) > 0 or bool(dict) :

        if bool(name) :

            print(f"Hello {name} This Is Your Score Table:")

        for d in dict :

            print(f"{d} => {dict[d]}")    

    else :

        print(f"Hello {name} You Have No Scores To Show")        



#get_the_scores("Osama", **scores_list)
#get_the_scores("Osama")
get_the_scores(**scores_list)
'''