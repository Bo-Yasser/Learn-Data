# timeit(stmt, setup, timer, number)
# timeit(pass, pass, default, 1.000.000) Default Value
import timeit
import random
# print(dir(timeit))

# print(timeit.timeit("'Elzero' * 1000"))

# name = "Elzero"
# print(name * 1000)

# print(timeit.timeit("name = 'Elzero'; name * 1000"))

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat= 4))




