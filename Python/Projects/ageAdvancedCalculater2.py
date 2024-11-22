agez = int(input("Please Enter Your Age : ").strip())



months1 = agez * 12
weeks1 = agez * 52.1
days1 = agez * 365.25
hours1 = days1 * 24
minutes1 = hours1 * 60
seconds1 = minutes1 * 60

mini= 10
max_age= 100


if max_age > agez :
    print("#"*80)

    print(" You Can Write The First Letter Or the Full Name Of The Time Unit ".center(80,"#"))

    print("#"*80)

    unit = input("Please Choose Time Unit \"Months, Weeks, Days, Hours, Minutes, Seconds, All\" : ").strip().lower()

    
    
    if unit == "all" or unit == "a" :
       print("You Choose All")
       print("\n")
       print(f"You Lived For \n{months1:,} Months.\n{weeks1:,} Weeks.\n{days1:,} Days.\n{hours1:,} Hours.\n{minutes1:,} Minutes.\n{seconds1:,} Seconds. ")
    elif unit == "months" or unit == "mo" :
       print("You Choose Months")
       print("\n")
       print(f"You Lived For {months1:,} Months. ")
 
    elif unit == "weeks" or unit == "w" :
       print("You Choose Weeks")
       print("\n")
       print(f"You Lived For {weeks1:,} Weeks. ")


    elif unit == "days" or unit == "d" :
       print("You Choose Days")
       print("\n")
       print(f"You Lived For {days1:,} Days. ")


    elif unit == "hours" or unit == "h" :
       print("You Choose Hours")
       print("\n")
       print(f"You Lived For {hours1:,} Hours. ")


    elif unit == "minutes" or unit == "mi" :
       print("You Choose Minutes")
       print("\n")
       print(f"You Lived For {minutes1:,} Minutes. ")        



    elif unit == "weeks" or unit == "w" :
       print("You Choose Seconds")
       print("\n")
       print(f"You Lived For {seconds1:,} Seconds. ")    


else: 
   print("Out Of Range")
