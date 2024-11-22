friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

a = 0
b = 0
while len(friends) > a :
    
    if friends[a].istitle() :
        print(friends[a])
     
    
    else : 
      b +=1
   
    a += 1 



print(f"Friends Printed And Ignored Names Count Is {b}")     