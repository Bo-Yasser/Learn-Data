
# this is comment

'''this is document'''
"""this is document"""

def elzero_Function(name):
    '''this is function to say hello from elzero
        it say hello from elzero

        parameter:
        name 
    '''
    print(f"Hello {name} From Elzero")



# elzero_Function("Ahmed") 

# print(dir(elzero_Function))

# print(elzero_Function.__doc__)
# help(elzero_Function)


def say_hello_to(name):
    
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    
    print(f"Hello {name}")

say_hello_to("Osama")
# help(say_hello_to)
print(say_hello_to.__doc__)