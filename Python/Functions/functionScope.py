
x = 1

def one():
    global x 
    x = 2
    print(f"Print Veriable From Function Scope insideFunction_one {x}")


def two():
    global x
    x = 4
    print(f"Print Veriable From Function Scope insideFunction_two {x}")





print(f"Print Veriable From Global Scope {x}")

print("-"*20)

one()
print(f"Print Veriable From Global Scope After Function_one Called {x}")

print("-"*20)

two()
print(f"Print Veriable From Global Scope After Function_two Called {x}")
