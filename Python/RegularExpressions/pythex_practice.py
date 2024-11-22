import re

# 1

# # ([A-z])\s



# my_string1 = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

# search1 = re.findall(r"([A-z])\s", my_string1)

# print(search1)

# for x in search1:

#     print(x, end="") # Elzero



# 2


# # L([A-z]+)

# my_string2 = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
# search2 = re.search(r"L([A-z]+)", my_string2)

# print(search2.group(1)) # Elzero



# 3

# # (\+?\(\d{4}\)\s\d+\-\d{4})
# my_string3 = """
# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234

# 01006001234
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12
# """

# search3 = re.findall(r"(\+?\(\d{4}\)\s\d+\-\d{4})", my_string3)

# print(search3)

# for z in search3 :
#     print(z)    # +(0100) 600-1234
#                 # +(0100) 60-1234
#                 # (0100) 6000-1234
    


# 4


# # (https?://(www\.)?\w+\.(com|org)(\:\d+)?/link(.+))

# my_string4 = """
# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py

# http://www.elzero.net
# https://elzero.net
# """
# search4 = re.findall(r"(https?://(www\.)?\w+\.(com|org)(\:\d+)?/link(.+))", my_string4, re.M)
# # print(search4)

# for g in search4 :
#     print(g[0])
# # http://www.elzero.org:8888/link.php  >> match 
# # https://elzero.org:8888/link.php     >> match 
# # http://www.elzero.com/link.py        >> match 
# # https://elzero.com/link.py           >> match 




# 5

# https?
# https|http
# h\w{3}s?
# h\w+
# [h-t]
# h.+
# \w+p\w?
# \wtt\w+

my_string5 = """
http
https
abcd
abcd
"""
my_methods = [r"https?", r"https|http", r"h\w{3}s?", r"h\w+", r"[h-t]", r"h.+", r"\w+p\w?", r"\wtt\w+"]

for t in my_methods:
    search5 = re.findall(t, my_string5)

    print(search5)

# http   >> match
# https  >> match
# abcd
# abcd