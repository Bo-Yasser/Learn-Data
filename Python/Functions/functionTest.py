

word = "wwwooooorrrlddd"


def rec(name):

    if len(name) == 1 :
    
        return name

    print(f"1- Print Start Function {name}")

    if name[0] == name[1]:

        print(f"2- Print Before Condition {name}")
        
        return rec(name[1:])   
    
    
    print(f"3- Print Before Return {name}")
    
    return name[0] + rec(name[1:])


print(rec("wwwooooorrrlddd"))