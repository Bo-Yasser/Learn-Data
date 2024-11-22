# fName = input('what\'s your first name : ').strip(" #@").capitalize()
# mName = input('what\'s your middle name : ').strip(" #@").capitalize()
# lName = input('what\'s your last name : ').strip(" #@").capitalize() 



# print(f'Hello {fName} {mName:.1s} {lName} Happy To See You')



from cs50 import get_int, get_float, get_string


# num1 = get_int("Enter Number One: ")
# num2 = get_int("Enter Number Two: ")
# print(num1 + num2)

# fnum1 = get_float("Enter Number One: ")
# fnum2 = get_float("Enter Number Two: ")
# print(fnum1 + fnum2)

string1 = get_string("Enter Name: ")
print(string1[-1::-1])