


# 1

# num = input("Add Your Number ").strip()


# if len(num) > 1 :
    
#     if num.isalpha() :
#         raise Exception("Only Numbers Allowed")
    
#     if num.isdigit():
#         raise IndexError(f"Only One Character Allowed")   



# elif int(num) == 0 :

#     raise ValueError("Number Must Be Larger Than 0")

# else:
#     print("#"* 20)
#     print(f"The Number Is {num}")
#     print("#"* 20)



# 2




try:

    LETTER = input("Add Letter From A to Z: ")
    

    if LETTER.isalpha():

        if len(LETTER) > 1 :
            raise NameError
    
        if not LETTER.isupper() : 
            raise IndexError 
    
    if LETTER.isdigit():

        raise Exception    



except NameError:
    print("You Must Write One Character Only")
except IndexError:
    print("The Letter Not In A - Z")
except Exception:
    print("Only Letters Allowed")    
else:
    print(f"You Typed {LETTER}")

