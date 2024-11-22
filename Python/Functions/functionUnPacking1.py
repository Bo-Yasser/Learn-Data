"""

list = [1, 2, 3, 4]

print(*list)"""


"""def say_hello(*peoples) : 

    

    for name in peoples :

        print(f"Hello {name}")


say_hello("Osama", "Ahmed", "Sayed", "Mahomud", "Zyad")"""



def show_details(name,*skills) :

    
    
    print(f"Hello {name} Your Skills Is : ")
    
    for skill in skills :

        print(skill)

show_details("Osama", "Html", "CSS", "JS")

show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")
 
