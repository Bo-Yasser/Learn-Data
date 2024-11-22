# 1
'''
num = int(input("Enter Your Number : "))

if num < 0 :
    print("NUmber 0 IS Not Larger Than 0 ")

else:
    sum = 0
    while num > 1 :
        
        num -=1
        if num == 6 :
            continue
        
        
         
        sum +=1  
        print(num)


print(f"{sum} Numbers Printed Successfuly ")


'''

# 2
'''
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

a = 0
b = 0
while len(friends) > a :
    
    if friends[a].istitle() :

        print(friends[a])

    
    
    else:        
        b +=1   
    a +=1

else:
    print(f"Friends Printed And Ingored Names Count Is {b}")
'''



# 3

'''
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

    print(skills.pop(0)) '''



# 4

my_friends = []

max = 4

while len(my_friends) < 4 :
    
    name = input("Please Enter Your Name : ")

    if name.isupper()  :

        print("Invalid Name")
        continue
    
    

  
    if name.islower() :

        my_friends.append(name.capitalize().strip())    
        
        print(f"Friend {name.strip().capitalize()} Added And First Letter Become Capital ")
    
    
    
    if name.istitle() :


        my_friends.append(name.strip()) 

        print(f"Friend {name.strip()} Added")
    
 
    print(my_friends)
    max -=1
    
    
    if max == 0 :
        
        print("List Is Full")
        break
    
    print(f"{"Last" if max == 1 else max} Chance Left" )   
    