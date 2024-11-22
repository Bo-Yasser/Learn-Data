country = "KSA"

if country == "Egypt": print(f"The Weather in {country} Is 15")


elif country == "KSA": print(f"The Weather In {country} Is 30")    


else: print("Country Is Not In The List")

#Short if

movieRate = 18
age = 16

if age < movieRate :
    print("Movie Is Not Good For You ")

else:
    print("Movie Is Good For You And Happy Watching")


print("Movie Is Not Good For You" if age < movieRate  else "Movie Is Good For You And Happy Watching")