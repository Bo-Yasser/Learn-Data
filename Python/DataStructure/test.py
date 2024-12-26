def s(exp):
    i = 0
    postfix = ""
    num = ""
    for i in exp:
        if i.isdigit():
            num += i
        else:
            if num:
                postfix += num + " "
                num = ""
    return postfix



print(s("555 + 333 + 222 - 11 1"))