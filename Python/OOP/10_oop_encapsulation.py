


# public
# protected
# private

# # 1
# class MemberOne:

#     def __init__(self, name):

#         self.name = name   # public

# one = MemberOne("Osama")
# print(one.name)
# one.name = "Sayed"
# print(one.name)

# # 2

# class MemberTwo:

#     def __init__(self, name):

#         self._name = name # protected _attribute

# Two = MemberTwo("Osama")
# print(Two._name)
# Two._name = "Sayed"
# print(Two._name)





class MemberThree:

    def __init__(self, name):

        self.__name = name # private __attribute

    def say_hello(self):

        return f"Hello {self.__name}"

three = MemberThree("Osama")
# print(three._name)
# three._name = "Sayed"        # give error
# print(three._name)

print(three.say_hello())

print(three._MemberThree__name)
three._MemberThree__name = "Ahmed"
print(three._MemberThree__name)

print(MemberThree('Mohamed')._MemberThree__name)



class MemberInheritance(MemberThree):

    def __init__(self, name):

        MemberThree.__init__(self, name)


print(MemberInheritance('Sayed')._MemberThree__name)