


def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4

#print(myGenerator)

myGen = myGenerator()


print(next(myGen))

print("Hello From Python")

print(next(myGen))

print("Hello From Python")

#print(next(myGen))

#print("Hello From Python")

#print(next(myGen))

print("#"*50)

for n in myGen:

    print(n)



    