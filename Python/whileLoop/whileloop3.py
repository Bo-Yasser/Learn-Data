myFavouriteWebs = []

maximumWebs = 5

a = 0

while maximumWebs > 0 :

    web = input("Web Site Name Without \'https://\' :")
    
    myFavouriteWebs.append(f"https://{web.strip(" !@#$%^&*()-+=").lower()}")

    maximumWebs -= 1

    print(f"Website Added, {maximumWebs} Places Left ")

    print(myFavouriteWebs)

    #print(myFavouriteWebs[a])

    #a += 1

else:
    print("Book Mark Is Full, You Cant Add More")    


if len(myFavouriteWebs) > 0 :

    #sort
    myFavouriteWebs.sort()

    index = 0

    print("Printing The List Of Websites In Your Bookmark ")

    while index < len(myFavouriteWebs) :

        print(myFavouriteWebs[index])

        index += 1

