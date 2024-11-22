admins = ["Ahmed", "Osama", "Sameh","Manal", "Rahma", "Mahmoud", "Enas",1]

name = input("Please Enter Your Name : ").strip().capitalize()

max = 8


if name in admins :
    
    print(f"Hello {name} Welcome Back")
    print("\n")
    print("Write Full Name For Your Choose Or Just First Letter ")

    option = input("Delete Or Update Your Name : ").strip().capitalize()
    
    

    # Update Option 
    if option == "Update" or option == "U":
        
        theNewName = input("Please Enter The New Name : ").strip().capitalize()
        
        print(f"Welcome {theNewName}")
        
        admins[admins.index(name)] = theNewName
        
        print("Name Updated")

        print(admins)

    # Delete Option
    elif option == "Delete" or option == "D":
          

        admins.remove(name)
        
        print("Name Deleted")

        print(admins)
    
    # Wrong Option
    else:
    
     print("Wrong Option")    
    



 

else: 
    

    status = input("You Are Not Admin, You Want To Join Us Yes, No ? \nWrite Full Name For Your Choose Or Just First Letter : \n").strip().capitalize()  
    
    if status == "No" or status == "N":


        print("Good Luck")

    elif len(admins) <= max :
       
       if status == "Yes" or status == "Y": 
        
        #newMember = input("Please Enter Your Name : ").strip().capitalize()

        admins.append(name)
        
        print(admins)

    elif len(admins) > max :



        print("Sorry List Is Full")



        
        
        
        

