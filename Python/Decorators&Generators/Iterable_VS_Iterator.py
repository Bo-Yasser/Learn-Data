

name = "Osama"
myList = [1, 2, 3, 4, 5]
myNumber = 10 

for n in name :     #by defult iter() #iter(name): ##same thing##         

    print(n, end=" ")



for l in myList:    #by defult iter() #iter(myList): ##same thing##

    print(l, end=" ")    

print()




myIterator = iter(name)
myIteratorList = iter(myList)

print(next(myIterator), end=" ")
print(next(myIterator), end=" ")
print(next(myIterator), end=" ")
print(next(myIterator), end=" ")
print(next(myIterator), end=" ")


print(next(myIteratorList), end=" ")
print(next(myIteratorList), end=" ")
print(next(myIteratorList), end=" ")
print(next(myIteratorList), end=" ")
print(next(myIteratorList), end=" ")