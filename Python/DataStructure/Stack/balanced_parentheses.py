import linked_stack as ls
def are_pair(open, close):
    pairs = {"(" : ")" ,"[" : "]" ,"{" : "}"}
    return pairs[open] == close

def are_balanced(exp):
    exp = str(exp)
    stack = ls.LinkedStack()
    for i in range(len(exp)):
        if exp[i] == "(" or exp[i] == "[" or exp[i] == "{":
            stack.push(exp[i])
        elif exp[i] == ")" or exp[i] == "]" or exp[i] == "}":
            if stack.is_empty() and not are_pair():
                return False
            else:
                stack.pop()
    
    return stack.is_empty()


print(are_balanced((5+2)*[4+3]+[3+1]))
print(are_balanced("(((({{{}}}))))[[[[[[(())]]]]]][((({{[[]]}})))]"))
print(are_balanced("[[[[[(("))