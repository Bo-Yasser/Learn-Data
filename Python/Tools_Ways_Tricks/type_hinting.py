'''module docstring'''

def say_hello(name) -> str:
    '''function one docstring'''
    print(f"Hello {name}")


say_hello("Ahmed")

def calculate_one(n1, n2) -> int:
    '''function two docstring'''
    print(n1 + n2)

calculate_one(10, 40)

def calculate_two(n1, n2) -> float:
    '''function three docstring'''
    print(n1 + n2)

calculate_two(10, 40)




def cc(num1, num2) -> int:

    """
    CC function docstring
    """
    return num1 + num2

print(cc(20, 30))
