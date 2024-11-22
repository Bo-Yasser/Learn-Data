name = """'Mohamed'"""
country = "Egypt"
age = '''"22"\"'''

#print("Hello "+name+", How You Doing \\\n\"\"\" Your Age Is "+age+" + \nAnd Your Country Is: "+country)


name2 = "Elzero"

#print(name2[-2::-2])

name3 = "#@#@Elzero#@#@"

#print(name3.strip("#@"))




num1 = "1"
num2 = "10"
num3 = "100"
num4 = "1000"

#print(num1.zfill(4))
#print(num2.zfill(4))
#print(num3.zfill(4))
#print(num4.zfill(4))




name4= "Osama"
name5 = "Osama_Elzero"

#print(name4.rjust(20,"@"))
#print(name5.rjust(20,"@"))


name6 = "OsAmA"
name7 = "eLZeRo"
#print(name6.swapcase())
#print(name7.swapcase())

msg = "I Love Python And Although Love Elzero Web School"

#print(msg.count("Love"))

name8 = "Elzero"

#print(name8.index("z"))
#print(name8.find("z"))

msg2 = "I <3 Python And Although <3 Elzero Web School"

#print(msg2.replace("<3", "Love" , 1))
#print(msg2.replace("<3","Love"))


namef = "Mohamed"
agef = 22
countryf = "Egypt"

#print("My Name Is {}, And My Age Is {}, And My Country Is {} ".format(namef,agef ,countryf))



#print(1)
#print(-1)
#print(1.00)
#print(1+1j)

complexnum = 1+2j

#print(complexnum.real)
#print(complexnum.imag)

num9 = 10
#print(float(num9))


num10 = 159.650

#print(int(num10))

#print(100 - 115)
#print(50 * 30)
#print(21 % 4)
#print(110 / 11)
#print(117 // 20)

#index & slicing
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

#print(friends[0])
#print(friends[-5])

#print(friends[4])
#print(friends[-1])

#print(friends[0::2])
#print(friends[1::2])


#print(friends[1:4])
#print(friends[3:5])


#list

#friends[3] = "Elzero"
#friends[4] = "Elzero"

#print(friends)


friendsx = ["Osama", "Ahmed", "Sayed"]

#friendsx.insert(0,"Nasser")
#print(friendsx)

#friendsx.append("Salem")

#print(friendsx)


X = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

#X.remove("Nasser")
#X.remove("Osama")

#print(X)

#X.pop()
#print(X)


friendsg = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]


#friendsg.extend(employees)
#friendsg.extend(school)

#print(friendsg)

friendsr = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

#friendsr.sort()
#print(friendsr)

#friendsr.sort(reverse=True)
#print(friendsr)

#print(len(friendsr))


technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]


#print(technologies[4][0])

#print(technologies[4][2])



tuple1 = "Osama",

#print(tuple1)

#print(type(tuple1))




tuple2 = ("Osama", "Ahmed", "Sayed")

#print(len(tuple2))


nums = (1, 2, 3)
letters = ("A", "B", "C")

#nums += letters

#print(nums)

#print(len(nums))




my_tuple = (1, 2, 3, 4)


#a, b, _, c = my_tuple

#print(a)
#print(b)
#print(c)




my_list = [1, 2, 3, 3, 4, 5, 1]

uniqe_list = [1, 2, 3, 4, 5]

#print(uniqe_list)

#print(type(uniqe_list))

#print(uniqe_list[:4])




nums2 = {1, 2, 3}
letters2 = {"A", "B", "C"}

#print(nums2 | letters2)
#print(nums2.union(letters2))
#nums2.update(letters2)
#print(nums2)


my_set = {1, 2, 3}
letters3 = {"A", "B", "C"}


#print(my_set)

#my_set.clear()
#print(my_set)

#my_set.add("A")
#my_set.add("B")
#print(my_set)

#my_set.discard("C")

#print(my_set)




set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

#print(set_one.issubset(set_two))

#print(set_two.issuperset(set_one))




dict1= {
    "Html" : "Html Progress Is 20%",
    "Css" : "Css Progress Is 30%",
    "Python" : "Python Progress Is 40%"
}


#print(dict1.get("Html"))
#print(dict1.get("Css"))
#print(dict1.get("Python"))

#dict1.update({"AI" : "AI Progress Is 70%"})

#print(dict1["AI"])



#print(bool(True))
#print(bool("S"))
#print(bool(8))
#print(bool(100.0))

#print(bool(False))
#print(bool(""))
#print(bool([]))
#print(bool(None))


html = 80
css = 60
javascript = 70

#print(html and css and javascript > 50)


nums3 = 10
nums4 = 20
numsall = 20

#print(numsall > nums3)

#print(numsall > nums4 > nums3)


nums5 = 10
nums6 = 20

#result = nums5 + nums6

#print(result)
#print(result**3)

#print(27000 // 27)

#print(1000/5)

#print(type(str(200.0)))


#namein = input("Please Enter Your Name : ").strip().capitalize()


#print(f"Hello {namein}, Happy To See You Here.")


#agein = int(input("Please Enter Your Age : "))

#if agein < 16 :
    #print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

#elif agein > 16 :
    #print(f"Hello Your Age Is {agein}, All Articles Is Suitable For You") 




#first_name = input("Please Enter Your First Name : ").strip().capitalize()    
#second_name = input("Please Enter Your Second Name : ").strip().capitalize()   

#print(f"Hello {first_name:s} {second_name:.1s} ")

#email = input("Please Enter Your Email : ").strip().lower()

#Namec = email[:email.index("@")].capitalize()

#webc = email[email.index("@") + 1 : email.index(".")]
#domain = email[email.index(".") + 1: ]

#print(f"Your Name Is {Namec} ")

#print(f"Your Website Is {webc} ")

#print(f"Your Website Is {domain} ")



#numq = input("Please Enter First Number : ").strip()
#numq2 = input("Please Enter Second Number : ").strip()

#operation = input("Enter Operator : ").strip()
#operators = ["+", "-", "*", "/", "%"]

#numq = int(numq) 
#numq2 = int(numq2)


#if operation in operators :
    #print(numq + numq2)

#elif operation in operators :
    #print(numq - numq2)

#elif operation in operators :
    #print(numq * numq2)

#elif operation in operators :
    #print(numq / numq2)        

#elif operation in operators :
    #print(numq % numq2)        





ager = 15


#if ager > 16 :
    #print("App Is Suitable For You")

#elif ager < 16 :
    #print("App IS Not suitable For You")    




#agez = int(input("Please Enter Your Age : ").strip())



#months1 = agez * 12
#weeks1 = agez * 52.1
#days1 = agez * 365.25
#hours1 = days1 * 24
#minutes1 = hours1 * 60
#seconds1 = minutes1 * 60

#mini= 10
#max_age= 100


#if max_age > agez > mini :
    #print("#"*80)

    #print(" You Can Write The First Letter Or the Full Name Of The Time Unit ".center(80,"#"))

    #print("#"*80)

    #unit = input("Please Choose Time Unit \"Months, Weeks, Days, Hours, Minutes, Seconds, All\" : ").strip().lower()

    
    
    #if unit == "all" or unit == "a" :
       #print("You Choose Weeks")
       #print("\n")
       #print(f"You Lived For \n{months1:,} Months.\n{weeks1:,} Weeks.\n{days1:,} Days.\n{hours1:,} Hours.\n{minutes1:,} Minutes.\n{seconds1:,} Seconds. ")
    #elif unit == "months" or unit == "ma" :
       #print("You Choose Months")
       #print("\n")
       #print(f"You Lived For {months1:,} Months. ")
 
    #elif unit == "weeks" or unit == "w" :
       #print("You Choose Weeks")
       #print("\n")
       #print(f"You Lived For {weeks1:,} Weeks. ")


    #elif unit == "days" or unit == "d" :
       #print("You Choose Days")
       #print("\n")
       #print(f"You Lived For {days1:,} Days. ")


    #elif unit == "hours" or unit == "h" :
       #print("You Choose Hours")
       #print("\n")
       #print(f"You Lived For {hours1:,} Hours. ")


    #elif unit == "minutes" or unit == "mi" :
       #print("You Choose Minutes")
       #print("\n")
       #print(f"You Lived For {minutes1:,} Minutes. ")        



    #elif unit == "weeks" or unit == "w" :
       #print("You Choose Seconds")
       #print("\n")
       #print(f"You Lived For {seconds1:,} Seconds. ")    


#else: 
   #print("Out Of Range")



#countrye = input("Please Enter Your Country : ").strip().capitalize()

arabcountries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "Bahrain"]
strangercountries = ["Canada", "Usa", "England"]

price = 100

discountearab = 50

discountestranger = 30

#if countrye in arabcountries : 
    
    #print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discountearab}$")


#elif countrye in strangercountries : 

    #print(f"Your Country Not Eligible For Discount And The Price Is {price - discountestranger}$" )

#else: 
    #print(f"You Have No Discount Price Is {price}$")





numw = int(input("Enter Number Please : ").strip())

if numw == 0 :
    
    print("Number 0 Is Not Larger Than 0")

else : 

    sum = 0
    while numw > 1 : #0 :

        numw -= 1
        
        if numw == 6 :
            continue
        
        #if numw == 0 :
            #break

        print(numw)
        sum +=1


print(f"{sum} Numbers Printed Successfully.")
