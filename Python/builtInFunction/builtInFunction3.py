
# abs()
# pow(num, exp, mod)
# min()
# max()
# slice()

# 1
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))


print("#" * 50)
print()

# 2

print(pow(2, 5))
print(pow(2, 5, 10))


print("#" * 50)
print()

# 3

print(min(1, 10, -50, 30))
print(min("A", "X", "Z", "Osama"))

myNumbers = (1, 20, -50, -100, 100)
print(min(myNumbers))

print("#" * 50)
print()


# 4

print(max(1, 10, -50, 30))
print(max("A", "X", "Z", "Osama"))

myNumbers2 = (1, 20, -50, -100, 100)
print(max(myNumbers2))

print("#" * 50)
print()


# 5

a = ["A", "B", "C", "D", "E", "F"]

print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
print(a[slice(2, 6, 2)])


