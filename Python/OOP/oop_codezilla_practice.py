
# # 1
# class Student:

#     no_of_students = 0
#     @classmethod
#     def class_method(cls):

#         return f"Class Method"
    
#     def __init__(self, name, age= 0, courses= "none"):

#         self.__name = name
#         self.__age = age
#         self.__courses = courses
#         Student.no_of_students += 1

#     def describe(self):
#         print(f"My Name Is {self.__name} And My Age Is {self.__age} ")

#     def is_old(self, num):
#         if self.__age <= num:
#             print("Student Is Old")

#         else:
#             print("Student Is Not Old")    

#     def get_name(self):

#         return self.__name
#     def set_name(self, new_name):

#         self.__name = new_name
        
#     def get_age(self):

#         return self.__age
#     def set_age(self, new_age):

#         self.__age = new_age
# student_1 = Student("Islam", 40, ["Science"])

# student_1.set_name("Mohamed")
# student_1.set_age(22)
# # student_1.describe()

# print(student_1._Student__name)





# # print(student_1.get_name())
# # student_1.set_name("Ahmed")
# # print(student_1.get_name())

# # student_2 = Student("Islam", 30, ["Cs", "Math"])
# # student_3 = Student("Ibrahim", 20, ["Cs", "Math"])
# # student_1.is_old(20)

# # print(id(student_1), id(student_2), sep="\n")
# # print(student_1 == student_2)
# # print(Student.class_method())





# # 2

# from datetime import date
# class StudentTwo:
    
  
#     def __init__(self, name, age= 0):

#         self.name = name
#         self.age = age


#     def describe_2(self):
#         print(f"My Name Is {self.name} And My Age Is {self.age} ")

#     @classmethod
#     def initFromBirthYear(cls, name, birthYear):

#         return cls(name, date.today().year - birthYear)
    



# student_one = StudentTwo("Ahmed", 20)
# student_two = StudentTwo.initFromBirthYear("Mohamed", 2002)

# student_one.describe_2()
# student_two.describe_2()

# # 3

# class Math:

#     @staticmethod
#     def add(x, y):
#         return x + y
#     @staticmethod
#     def add5(num):
#         return num + 5
#     @staticmethod
#     def add10(num):
#         return num + 10
#     @staticmethod
#     def PI():
#         return 3.14



# # x = Math.add(5, 10)
# # y = Math.add5(x)
# # z = Math.add10(y)
# # print(x, y, z)


# class Pizza:

#     def __init__(self, radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients

#     def __str__(self):
#         return f"Pizza Ingredients Are {self.ingredients}" 
    
#     def area(self):
#         return Pizza.circle_area(self.radius)
#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * Math.PI()


# p = Pizza(6, ["mozzarelaa", "tomatoes"])
# print(p.area())
# print(Pizza.circle_area(4))
# print(Pizza.circle_area(10))


# 5 

# class Dates:
#     def __init__(self, date):
#         self.__date = date

#     def get_date(self):
#         return self.__date
#     @staticmethod
#     def to_dash_date(date):
#         return date.replace("/", "-")
# ddate = Dates("15-12-2016")
# date_from_db = "15/12/2016"
# date_with_dash = Dates.to_dash_date(date_from_db)
# print(date_with_dash)
# if ddate.get_date() == date_with_dash:
#     print("Equal")
# else:
#     print("Unequal")




# 6
# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f"Name Is {self.name} And Age Is {self.age}"

#     @classmethod
#     def init_From_birth_year(cls, name, birthyear, extra= "Unknown"):
#         return cls(name, date.today().year - birthyear, extra)



# class Man(Person):
#     gender = "Male"
#     no_of_men = 0

#     def __init__(self, name, age, voice):
#         super().__init__(name, age)
#         self.voice = voice
#         Man.no_of_men += 1
    
#     def display(self):
#         string = super().display()
#         return string + f" And Voice Is {self.voice} And Gender Is {Man.gender}"

# man1 = Man("Mohamed", 22, "Hard")
# man2 = Man.init_From_birth_year("Mohamed", 2002, "Hard")
# print(Man.no_of_men)
# print(man1.display())
# print(man2.display())

# class Woman(Person):
#     gender = "Female"
#     no_of_woman = 0

#     def __init__(self, name, age, hair):
#         super().__init__(name, age)
#         self.hair = hair
#         Woman.no_of_woman += 1
    
#     def display(self):
#         string = super().display()
#         return string + f" And Hair Is {self.hair} And Gender Is {Woman.gender}"

# woman1 = Woman("Shimaa", 20, "Curly")
# woman2 = Woman.init_From_birth_year("Shimaa", 2004, "Curly")

# print(woman1.display())
# print(woman2.display())

# print(Woman.no_of_woman)

# print(isinstance(woman1, Woman))




from abc import ABC, ABCMeta, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4

class Rect(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return (self.__length + self.__width) * 2

square = Square(10)
print(f"Square Area Is {square.area()} And Perimeter Is {square.perimeter()}")
rect = Rect(5, 3)
print(f"Rectangle Area Is {rect.area()} And Perimeter Is {rect.perimeter()}")