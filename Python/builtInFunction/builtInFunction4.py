
# 1

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 1)

#print(type(mySkillsWithCounter))

#for counter, skill in mySkillsWithCounter :

    
    #print(f"{counter} - {skill}")

print("#" * 50)

# 2

#print(help(print))


print("#" * 50)


# 3

myString = "Elzero"

myList = ["Html", "Css", "Js", "PHP"]

print(reversed(myString))

for letter in reversed(myString) :

    print(letter, end="")

print(f"\n{myString[::-1]}")    


for argu in reversed(myList) :

    print(argu, end="")

print(f"\n{myList[::-1]}")    

