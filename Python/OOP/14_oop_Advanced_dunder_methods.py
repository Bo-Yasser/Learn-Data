class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        names = self.name + " And " + other.name
        ages = self.age + other.age
        return f"Name Combined Are {names} And Sum Of Ages Is {ages}"
    def __lt__(self, other):
        return self.age < other.age

    def display(self):
        
        return f"Name Is {self.name} And Age Is {self.age}"

man = Man("Mohamed", 22)
man2 = Man("Ahmed", 20)
print(man + man2)
print(man > man2)
print(man < man2)

