
age = int(input("Please Enter Your Age : ").strip())
print("#"*80)

print(" You Can Write The First Letter Or the Full Name Of The Time Unit ".center(80,"#"))

print("#"*80)

unit = input("Please Choose Time Unit : Months, Weeks, Days, Hours, Minutes, Seconds, All : ").strip().lower()
print("\n")


months = age * 12
weeks = age * 52.1
days = age * 365.25
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if unit == "all" or unit == "a" :
    print("You Choose All Units ")
    print("\n")
    print(f"You lived For \n{months:,} Months. \n{weeks:,} Weeks. \n{days:,} Days. \n{hours:,} Hours. \n{minutes:,} Minutes. \n{seconds:,} Seconds.")

elif unit == "months" or unit == "m":
    print("You Choose The Unit Months")
    print("\n")
    print(f"You Lived For {months:,} Months.")


elif unit == "weeks" or unit == "w":
    print("You Choose The Unit Weeks")
    print("\n")
    print(f"You Lived For {weeks:,} Weeks.")

elif unit == "days" or unit == "d":
    print("You Choose The Unit Days") 
    print("\n")      
    print(f"You Lived For {days:,} Days.")


elif unit == "hours" or unit == "h":
    print("You Choose The Unit Hours")
    print("\n")
    print(f"You Lived For {hours:,} Hours.")



elif unit == "minutes" or unit == "mi":
    print("You Choose The Unit Minutes")
    print("\n")
    print(f"You Lived For {minutes:,} Minutes.")



elif unit == "seconds" or unit == "s":
    print("You Choose The Unit Seconds")
    print("\n")
    print(f"You Lived For {seconds:,} Seconds.")    





