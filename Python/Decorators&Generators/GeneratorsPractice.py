

# 1

def reverse_string_1(my_string):

    yield my_string[-1]
    yield my_string[-2]
    yield my_string[-3]
    yield my_string[-4]
    yield my_string[-5]
    yield my_string[-6]




for c in reverse_string_1("elzero") :

    print(c, end="")

print()
    
def reverse_string_2(my_string):

    for x in my_string[-1::-1]:
        yield x




reverse_string_2("Elzero") 








