
class Skill:
    
    def __init__(self):
        self.skills = ["Html", "Css", "Js"]

    def __str__(self):
        return f"This Is My Skills => {self.skills}"
    def __len__(self):

        return len(self.skills)




profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(profile)
print(len(profile))


# print(profile.__class__)
# print("#"* 50)

# my_num = 10
# print(my_num.__class__)
# print("#"* 50)

# my_list = list(["Zezo", "Mezo", "Keko"])
# print(my_list.__class__)
# list.append(my_list, "Zere")
# print(my_list)
# list.append(list(["Zezo", "Mezo", "Keko"]), "Zere")
# print(my_list)
# print("#"* 50)

# my_string = str("Osama")
# print(type(my_string))
# print(my_string.__class__)
# print(my_string.upper())
# print(str.upper(my_string))
# print(str.upper(str("osama")))


# print(dir(str))
# print(dir(list))
# print(dir(type))
