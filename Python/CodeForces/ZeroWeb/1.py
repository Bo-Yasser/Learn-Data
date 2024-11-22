# Code Wars

# multiply

# def simple_multiplication(number) :
#     if number % 2 == 0:
#         return number * 8 
#     else:
#         return number * 9

# print(simple_multiplication(1)  )      


# 2
# from math import *

# # print(ceil(123 / 10))
# def century(year):
#     if year % 100 == 0:
#         return year // 100 
#     else:
#         return year // 100 + 1

    
# print(century(2001))

# 3

# n = 12
# x = 7
# y = 5
# def is_divisible(n,x,y):
#     if n % x == 0 and n % y == 0:
#         return True

    
#     return False

# def is_divisible(n,x,y):
#     return n % x == 0 and n % y == 0 ;True;False

# print(is_divisible(3, 3, 4))


# 4 
# def even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     elif number % 2 != 0:
#         return "Odd"
# def even_or_odd(number):


#     return f"Even" if number % 2 == 0 else "Odd"


# print(even_or_odd(4))


# 5

# def solution(string):
#     return string[::-1]
# def solution(string):
#     return string[-1::-1]

# def solution(string):
#     newstring = ""
#     index = len(string) - 1
#     for s in string:
#         s = string[index]
#         newstring += s
#         index -= 1 
#     return newstring
# print(solution("world"))

# 6
# def boolean_to_string(b):
#     if bool(b):
#         return "True"
#     else:
#         return "False"
# def boolean_to_string(b):
#     if b:
#         return "True"
#     else:
#         return "False"
# def boolean_to_string(b):    
#     return str(b)

# print(boolean_to_string(True))    

# 7

# def mango(quantity, price):
    
#     if quantity >= 3:
#         free = quantity // 3
#         newq = quantity - quantity // 3
#         return newq * price
#     else:
#         return "no mango for free"
    

# def mango(quantity, price):
#     return (quantity - quantity // 3) * price

# def mango(quantity, price):
#     return ((quantity - int(quantity/3))  * price)

# print(mango(8, 5))


# 8

# def quarter_of(month):
#     if month < 4:
#         return 1
#     elif month < 7:
#         return 2   
#     elif month < 10:
#         return 3    
#     elif month < 13:
#         return 4    
    

# from math import ceil
# def quarter_of(month):
#     return ceil(month / 3)
# print(quarter_of(8))    


# 9
# def invert(lst):
#     lst2 = []
#     for i in lst:
#         lst2.append(i * -1)
    
#     return lst2 


# def invert(lst):
    
#     return [i*-1 for i in lst]

# print(invert([1, 2, 3, 4, 5]))



# 10

# def remove_exclamation_marks(string):
#     new_string = ""
#     for s in string:
#         if s == "!":
#             continue
#         else:
#             new_string += s
#     return new_string            


# def remove_exclamation_marks(string):
#     new_string = ""
#     for s in string:
#         if s != "!":
#             new_string += s 

#     return new_string            

# def remove_exclamation_marks(string):
#     return string.replace("!", "")


# def remove_exclamation_marks(string):   # just back list 
#     new_string = ""
#     return [s for s in string if s != "!"]
# print(remove_exclamation_marks("!!moha!!med!!"))

# 11


# def minimum(arr):
#     min = arr[0]
#     for a in arr:
#         if a < min:
#             min = a

#     return min            


# def maximum(arr):
#     max = arr[0]
#     for a in arr:
#         if a >  max:
#             max = a

#     return max           


# def maximum(arr):

#     return sorted(arr)[-1]
# def minimum(arr):

#     return sorted(arr)[0]


# print(minimum([4,6,2,1,9,63,-134,566]))

# print(maximum([4,6,2,1,9,63,-134,566]))


# 12


# def litres(time):
    
    
#     return int(time * .5)
# def litres(time):
#     return time // 2

# from math import floor 
# def litres(time):
    
    
#     return floor(time * .5)


# 13

# def grow(arr):

#     index = arr[0]
#     for a in arr[1:]:
#         index *= a 
#     return index
# from functools import reduce 
# def grow(arr):
    
#     return reduce(lambda x, y: x * y, arr) 

# print(grow([1, 2, 3, 4]))


# 14
# def string_to_number(s):
#     return int(s)

# 15
# def remove_char(s):
#     return s[1 : -1]

# def remove_char(str):
#     result = ""
    
#     for s in str[1:-1]:
        
#         result += s 
    
#     return result

# print(remove_char("ok"))

# 16

# def repeat_str(repeat, string):
#     return string * repeat


# 17

# def no_space(space):
#     new_string = ""
#     for s in space:
#         if s == " ":
#             continue
#         new_string += s 
    
#     return new_string

# def no_space(space):
#     new_string = ""
#     for s in space:
#         if s.isspace():
#             continue
#         new_string += s 
    
#     return new_string

# def no_space(space):
#     return space.replace(" ", "")
# def no_space(space):
#     return "".join(space.split())

# print(no_space("m o h a med"))



# 18

# def str_count(strng, letter):
#     return strng.count(letter)

# def str_count(strng, letter):
#     count = ""
#     for s in strng:
#         if s == letter:
#             count += s
#     return len(count)

# def str_count(strng, letter):
#     counter = 0
    
#     for chr in strng:
#         if chr == letter:
#             counter += 1
#     return counter        

# print(str_count("Hello", "l"))



# 19
# def past(h, m, s):
#     one_second = 1000
#     one_minute = 60 * one_second
#     one_hour = 60 * one_minute
#     return (h * one_hour) + (m * one_minute) + (s * one_second) 

# def past(h, m, s):

#     return (h * 3600 + m * 60 + s ) * 1000

# print(past(1, 2, 3))


# 20

# def to_alternating_case(string):
#     new= ""
#     for s in string:
#         if s.isupper():
#             new += s.lower()
#         elif s.islower():
#             new += s.upper()
#         else:
#             new += s          
#     return new
# def to_alternating_case(string):
#     return string.swapcase()    

# print(to_alternating_case("HeLLo WoRLD"))

# 21


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if mpg * fuel_left >= distance_to_pump:
#         return True
#     else:
#         return False

# def zero_fuel(distance_to_pump, mpg, fuel_left):

#     return mpg * fuel_left >= distance_to_pump;True;False

# def zero_fuel(distance_to_pump, mpg, fuel_left):

#     return mpg * fuel_left >= distance_to_pump    

# print(zero_fuel(100, 50, 1))


# 22

# def is_uppercase(inp):
#     for i in inp:
#         if i.islower():
#             return False
    
#     return True

# def is_uppercase(inp):
    
#     return inp == inp.upper()


# class Word:
    
#     def __init__(self,string=None):
#         self.string = string
    
#     def isup(self,string):
#         if ord(string)-96 > 0:
#             if not string.isalpha():
#                 return True 
#             return False
#         return True
        
#     def is_upper(self):
#         string = self.string
#         for i in range(len(string)):
#             if not (self.isup(string[i])):
#                 return False
#         return True
        


# def is_uppercase(string):
#     a = Word(string)
#     return a.is_upper()    

# print(is_uppercase("T0/kp"))    



# 23
# def basic_op(operator, value1, value2):
    
#     if operator in ["+", "add"]:
#         return value1 + value2
#     elif operator in ["-", "sub"]:
#         return value1 - value2
#     elif operator in ["*", "multiply"]:
#         return value1 * value2
#     elif operator in ["/", "div"]:
#         return value1 / value2 

# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))


# m = "20"
# o = "+"
# print(eval(m))
# print(type(eval(m)))
# print(type(eval(o)))


# 24
# def count_sheeps(sheep):
#     new = []
#     for s in sheep:
#         if s:
#             new.append(s)
        
    
#     return len(new)

# def count_sheeps(sheep):
#     return sheep.count(True) 

# def count_sheeps(sheep):
#     return len([s for s in sheep if s])    

    
# print(count_sheeps([True,  True,  True,  False,
#                   True,  True,  True,  True ,
#                   True,  False, True,  False,
#                   True,  False, False, True ,
#                   True,  True,  True,  True ,
#                   False, False, True,  True ]))


# 25

# def square_sum(numbers):
    
#     if len(numbers) >= 1:
#         index = (numbers[0])**2
#         for n in numbers[1:]:
#             index += n**2
#         return index
#     else:
#         return 0
# def square_sum(numbers):
#     index = []
#     for x in numbers:
#         index.append(x ** 2)
#     return sum(index)
# # def square_sum(numbers):
# #     return sum(x ** 2 for x in numbers)
    
# print(square_sum([1,2]))    


# 26




# def odd_count(odd):
#     return odd // 2
# def odd_count(odd):
#     return int(odd / 2)
# from math import floor 
# def odd_count(odd):
#     return floor(odd / 2)

# def odd_count(odd):
#     return len(range(1, odd, 2))    


# def odd_count(n): return n>>1 # >> move to right in binary or bits men al a5r division on 2 n>>1 division on 2 one time n>>2 divison on 2 two times#    

# def odd_count(odd):

#     listt = []
#     if 0 < odd < 3:
#         listt.append(odd)
#     elif odd > 1:
#         listt = range(1, odd, 2)    
#     return len(listt)

# print(odd_count(0))    



# 27

# def get_real_floor(n):
#     if 0 < n <= 13:
#         return n - 1
#     elif n > 13:
#         return n - 2
#     else:
#         return n

# def get_real_floor(n):
#     return n - 1 if 0 < n <= 13 else n - 2 if n > 13 else n     

# def get_real_floor(n):
#     if n <= 0:
#         return n
#     return n - 1 - (n > 13)     
# def get_real_floor(n):
#     return n - (n > 0) - (n > 13)        #True = 1 False = 0#   #if all True n - 1 - 1#   #if all False n - 0 - 0#  

# print(get_real_floor(13))        



# 28
# def find_average(numbers):
#     return sum(numbers) / len(numbers) if len(numbers) > 0 else 0
# def find_average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0  

# def find_average(numbers):
#     try:
#         return sum(numbers) / len(numbers)
#     except ZeroDivisionError:
#         return 0
# def find_average(numbers):
#     if numbers:
#         index = numbers[0]
#         for n in numbers:
#             index += n
#         return (index - numbers[0]) / len(numbers)
#     else:
#         return 0    

# print(find_average([1, 2, 3]))



# 29
# def make_negative(n):
#     return n * -1 if n > 0 else n if n < 0 else 0

# def make_negative(n):
#     return n - n * 2 if n > 0 else n    

# def make_negative(n):
#     return -abs(n)    
# print(make_negative(0))




# 30

# def swap_values(args): 
#     args.reverse()

# def swap_values(args): 
#     n = 0
#     sorted_list = []
#     sorted_str = ""
#     index = len(args) - 1
#     if isinstance(args, (tuple, list)):
#         while len(args) > n:
#             sorted_list.append(args[index])
#             index -= 1
#             n +=1
#         return sorted_list      
#     elif isinstance(args, str):
#         while len(args) > n:
#             sorted_str += args[index]
#             index -= 1
#             n +=1
#         return sorted_str

# def swap_values(args):
#     args[0], args[1] = args[1], args[0]
#     return args
# def swap_values(args):
#     args[:]=args[::-1]
#     return args
          
# arr = [1, 2]
# print(swap_values(arr))


# 31

# def people_with_age_drink(age):
#     return  "drink whisky" if age > 20 else "drink beer" if 17 < age < 21 else "drink coke" if 13 < age < 18  else "drink toddy" 

# 32 
# def hero(bullets, dragons):
    
#     return bullets / 2 >= dragons;True;False    


# 33

# def correct(str):
#     new_str = "" 
#     for s in str:
#         if s == "1":
#             new_str += "I"
#         elif s == "5":
#             new_str += "S"            
#         elif s == "0":
#             new_str += "O"
#         else:
#             new_str += s    
#     return new_str

# def correct(str):
#     return str.replace("1", "I").replace("0", "O").replace("5", "S")
# def correct(s):
#     s = s.replace('0', 'O')
#     s = s.replace('1', 'I')
#     s = s.replace('5', 'S')
#     return s

# def correct(string):
#     dict = {'0' : 'O', '1' : 'I', '5' : 'S'}
#     new = ""
#     for i in string:
#         if i.isdigit():
#             new += dict[i]
#         else:
#             new += i
#     return new   
# def correct(string):
#     dict = {'0' : 'O', '1' : 'I', '5' : 'S'}
#     new = ""
#     for i in string:
#         if i.isdigit():
#             new += "".join([dict[i]])
#         else:
#             new += "".join([i])
#     return new 
# def correct(string):
#     dict = {'0' : 'O', '1' : 'I', '5' : 'S'}
#     return ''.join([dict[i] if i.isdigit() else i for i in string])

# print(correct("51NGAP0RE"))



# 34

# def rps(p1, p2):
#     msg = ""
#     p1win = "Player 1 won!"
#     p2win = "Player 2 won!"
    
#     if p1 == p2: msg = "Draw!"

#     if p1 == "rock":
#         if p2 == "paper": msg = p2win
#         if p2 == "scissors": msg = p1win
    
#     if p1 == "paper":
#         if p2 == "rock": msg = p1win
#         if p2 == "scissors": msg = p2win

#     if p1 == "scissors":
#         if p2 == "rock": msg = p2win
#         if p2 == "paper": msg = p1win

#     return msg

# def rps(p1, p2):
#     dict = {
#     "rock": "scissors",
#     "paper" : "rock",
#     "scissors" : "paper"
#     }
#     if dict[p1] == p2:
#         return "Player 1 won!"
#     if dict[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"        

# def rps(p1, p2):
#     d1 = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]
#     return "Draw!" if p1 == p2 else "Player {} won!".format(1 if (p1, p2) in d1 else 2)

# def rps(p1, p2):
#     dict = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[dict[p1] - dict[p2]]

# rps = lambda a, b: ['Draw!', 'Player 1 won!', 'Player 2 won!'][('srp'.index(a[0]) - 'srp'.index(b[0])) % 3]

     
# print(rps("rock", "paper"))        


# 35
# def greet(name):
 
#     return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)

# print(greet("Gamal"))

# 36

# def get_char(c):
#     return chr(c)

# get_char=chr

# print(get_char(36))

# 37
# def nth_even(n):
    # return n * 2 - 2

# 38
# def between(a,b):
#     if a < b:
#         return [r for r in range(a, b +1)]
# def between(a,b):
#     return list(range(a, b + 1))    
# print(between(1, 7))  


# 39

# def abbrev_name(name):
#     return (name[0]).capitalize()+"."+(name[name.index(" ") + 1]).capitalize()
# def abbrevName(name):
#     return '.'.join([w[0] for w in name.split()]).upper()
# print(abbrev_name("Evan C"))
# print(".".join("ahmed"))


# 40

# def make_upper_case(s):
#     return s.upper()


# 41

# def check(seq, elem):
#     return seq.count(elem) > 0
# def check(seq, elem):
#     return elem in seq

# def check(seq, elem):
#     for s in seq:
#         if s == elem:
#             return True
        
#     return False


# 41
# def switch_it_up(number):
#     dict = {0 : "Zero", 1 : "One", 2 : "Two",
#             3 : "Three", 4 : "Four", 5 : "Five",
#             6 : "Six", 8 : "Eight", 7 : "Seven",
#             9 : "Nine"
#         }
#     return dict.get(number)

# def switch_it_up(number):
#     return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][number]


# print(switch_it_up(1))

# 42
# def lovefunc( flower1, flower2 ):
#     r = flower1 + flower2
    
#     return r % 2 != 0

# print(lovefunc(1, 4))     


# 43

# def move(position, roll):
#     if 0 < roll < 7:
#         return position + roll * 2
# def move(position, roll):
#     return position + roll * 2        
# def move(position, roll):
#     return position + roll * 2 if 0 < roll < 7 else "Wrong Input" 

# print(move("1", 2))    


# 44

def sum_of_differences(arr):
    index = arr[0]
    list = []
    if len(arr) > 0:
        for a in arr[1:]:
            index -= a
            for i in arr[:]:
                index += a
        return index

print(sum_of_differences([-3, -2, -1]))
