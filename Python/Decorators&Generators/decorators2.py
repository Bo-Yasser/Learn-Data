def myDecorator(func):

    def nestedFunc(num1, num2):
        if num1 < 0 or num2 < 0 :

            print("Beware One Of The Numbers Less Than Zero")

        func(num1, num2)
    
    
    return nestedFunc



def myDecoratorTwo(func):

    def nestedFunc(num1, num2):

        print("Coming From Decorator Two")
        func(num1, num2)
    
    
    return nestedFunc


@myDecorator
@myDecoratorTwo
def calculate(n1, n2):

    print(n1 + n2)  

calculate(-5, 90)          