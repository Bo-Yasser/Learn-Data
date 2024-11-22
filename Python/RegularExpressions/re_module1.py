


# [A-z0-9\.]+@[A-z0-9]+\.(com|net|mail|org|info)

import re

# 1

# my_search= re.search(r"[A-Z]{2}", "OOsamaEElzero")

# print(my_search)

# print(my_search.span())
# print(my_search.group())

# print(my_search.string)



# 2

# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

# if is_email :

#     print("This Is A Valid Email")
    
#     print()

#     print(is_email)
#     print(is_email.span())
#     print(is_email.group())
#     print(is_email.string)



# else:
#     print("This Is Not A Valid Email")


# 3

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

    empty_list.append(search)

    print("Email Added")

else:

    print("Invalid Email")    


for email in empty_list:

    print(email)    


