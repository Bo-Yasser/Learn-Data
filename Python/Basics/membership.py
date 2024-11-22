name = "osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)


friends = ["Ahmed","Sayed","Mahmoud"]

print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" *50)

countriesOne = ["Egypt","KSA","Kuwait","Bahrain"]

countriesOneDiscount = 80

countriesTwo = ["Italy","USA"]
countriesTwoDiscount = 50

myCountry = input("Enter Your Country : ").strip(" !@#$%^&*()-_=+`~?/>.<,|\\\"{}")

if myCountry in countriesOne : 
    print(f"Hello You Have A Discount Equal To {countriesOneDiscount}$")


elif myCountry in countriesTwo:
    print(f"You Have A Discount Equal To {countriesTwoDiscount}$")

else : 
    print("You Have No Discount")    