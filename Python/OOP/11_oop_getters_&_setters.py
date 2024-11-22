




class MemberThree:

    def __init__(self, name):

        self.__name = name # private __attribute

    def say_hello(self):

        return f"Hello {self.__name}"
    
    def get_name(self):

        return self.__name

    def set_name(self, new_name):

        self.__name = new_name.capitalize()

        return self.__name

three = MemberThree("Osama")

# print(three._name)
# three._name = "Sayed"        # give error
# print(three._name)

# print(three.say_hello())

# print(three._MemberThree__name)
# three._MemberThree__name = "Ahmed"
# print(three._MemberThree__name)

# print(MemberThree('Mohamed')._MemberThree__name)

print(three.get_name())


three.set_name("mohsen")
print(three.get_name())