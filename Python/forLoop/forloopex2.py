start = int(input("Enter The Start Number : ").strip())

end = int(input("How Should I Go :").strip())




print("Number         Square")
print("-" * 25)


for i in range(start, end + 1) :
    
    print(f"{i:d} {" "*15} {i**2:d}")
    

    
    