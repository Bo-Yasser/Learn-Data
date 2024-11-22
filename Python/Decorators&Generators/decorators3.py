

from time import time

# def myDecorattor(func):


#     def nestedFunc(*numbers):
        
#         for number in numbers :       
#             if number < 0 :

#                 print("Beware One Of The Numbers Less Than Zero")
            
#         func(*numbers)

#     return nestedFunc


# def myDecorator2(func):

#     def nestedFunc(num1, num2):

#         print("Coming From Decorator Two")
#         print("Beware One Of The Numbers Less Than Zero")    
#         func(num1, num2)
#     return nestedFunc

# @myDecorattor

# def calculate(n1, n2, n3, n4):


#     print(n1 + n2 + n3 + n4)

# calculate(-5, 90, 50, 150)

# print("#"* 50)

# calculate(10, 90)


def speedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f"Running Time Is {end - start}")

    return wrapper
    
@speedTest
def bigLoop():

    for r in range(1, 20000):

        print(r)

bigLoop()
