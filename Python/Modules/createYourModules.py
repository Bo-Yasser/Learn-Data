

import sys

# sys.path.append(r"h:\Games")
# print(sys.path)

###################################################################
###################################################################


import firstCreate

print(dir(firstCreate))

firstCreate.sayHello("Osama")
firstCreate.sayHello("Ahmed")
firstCreate.sayHello("Mohamed")

firstCreate.sayHowAreYou("Osama")
firstCreate.sayHowAreYou("Ahmed")
firstCreate.sayHowAreYou("Mohamed")


print("#" * 50)
###################################################################
###################################################################


import firstCreate as e

print(dir(e))

e.sayHello("Osama")
e.sayHello("Ahmed")
e.sayHello("Mohamed")

e.sayHowAreYou("Osama")
e.sayHowAreYou("Ahmed")
e.sayHowAreYou("Mohamed")

print("#" * 50)
###################################################################
###################################################################


from firstCreate import sayHello 

sayHello("Osama")



from firstCreate import sayHello as s

s("Osama")

print("#" * 50)
###################################################################
###################################################################


from firstCreate import *

sayHello("Mohamed")
sayHowAreYou("Mohamed")
 

