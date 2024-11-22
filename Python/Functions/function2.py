#a, b, c = input("Enter Your Name : ")


#print(f"Hello {a}")
#print(f"Hello {b}")
#print(f"Hello {c}")


'''def say_hello(name):
    print(f"Hello {name}")


say_hello("Osama")    '''



def addition(n1, n2):

    if type(n1) != int or type(n2) != int :

        print("Only Numbers Allowed ")
    
    else:

        print(n1 + n2)


addition(100, 300)


def full_name(first, middle, last) :

    print(f"Hello {first.strip().capitalize()} {middle.strip().upper():.1s} {last.strip().capitalize()}")


full_name("    osama", "  mohamed" , "   elsayed  ")



