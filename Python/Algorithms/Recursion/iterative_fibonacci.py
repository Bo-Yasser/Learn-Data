def fib(n):
    if n <= 1:
        return n
    
    n1 = 0 
    n2 = 1
    n3 = int

    for i in range(2, n + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return n3

print(fib(40))
