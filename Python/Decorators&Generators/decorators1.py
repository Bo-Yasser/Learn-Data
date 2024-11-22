

def myDecorator(func):

    def nestedFunc():

        print("Before")

        func()

        print("After")


    return nestedFunc 
print(type(myDecorator))

@myDecorator
def sayHello():

    print("Hello From Say Hello Function")


#afterDecoration = myDecorator(sayHello)
#afterDecoration()

@myDecorator
def sayHowAreYou():
    print("Hello From Say How Are You Function")


sayHello()

print("#" * 50)

sayHowAreYou()