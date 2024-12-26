import stack as st

# Expression Evaluation Using Stack

def is_operand(exp):
    return exp.replace('.', '', 1).isdigit()  

def is_operator(op):
    return op in ["+", "-", "*", "/", "^"]

def has_higher_precedence(op1, op2):
    precedence = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 4}
    return precedence[op1] >= precedence[op2]


def infix_to_postfix(exp):
    stack = st.Stack(len(exp), "str")
    postfix = ""
    number = ""

    for char in exp:
        if char.isdigit() or char == '.':
            number += char  
        else:
            if number:
                postfix += number + " "
                number = ""
            
            if char == " " or char == ",":
                continue

            if is_operator(char):
                while not stack.is_empty() and stack.top() != "(" and has_higher_precedence(stack.top(), char):
                    postfix += stack.pop() + " "
                stack.push(char)

            elif char == "(":
                stack.push(char)

            elif char == ")":
                while not stack.is_empty() and stack.top() != "(":
                    postfix += stack.pop() + " "
                stack.pop()
    

    if number:
        postfix += number + " "

    while not stack.is_empty():
        postfix += stack.pop() + " "

    return postfix.strip()


def perform_operation(op1, op2, op):
    if op == "+":
        return op2 + op1
    elif op == "-":
        return op2 - op1
    elif op == "*":
        return op2 * op1
    elif op == "/":
        return float(op2) / float(op1)  
    elif op == "^":
        return op2 ** op1

def evaluate_postfix(exp):
    stack = st.Stack(1000, "float")
    tokens = exp.split()  

    for ch in tokens:
        if ch.replace(".", "", 1).isdigit():
            stack.push(float(ch))
        
        elif is_operator(ch):  
            op1 = stack.pop()
            op2 = stack.pop()
            result = perform_operation(op1, op2, ch)
            stack.push(result)


    return round(stack.top(), 2)


print(infix_to_postfix("12.5+23*(3.5 - 2.1)/4"))
print(evaluate_postfix("12.5 23 3.5 2.1 - * 4 / +"))



# (5*2^2)+(4/2^3)-(4*(3/2^2) + 1)-2
            
