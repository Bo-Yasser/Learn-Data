# https://www.elzero.org:8080/category.php?article=105?name=how-to-do
# https://www.elzero.org/category.php?article=105?name=how-to-do
# https://elzero.org/category=50?article=105?name=how-to-do

# http://elzero.org/category=50?article=105?name=how-to-do
# http://elzero.org
# http://elzero.net

import re
# (https?)://(www)?\.?(\w)+\.(\w+):?(\d+)?/?(.+)

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web, re.M )




# print(search.groups())



# for group in search.groups():
#     print(group)

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")

