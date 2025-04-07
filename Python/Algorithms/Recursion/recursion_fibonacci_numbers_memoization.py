def fib(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n

    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]

print(fib(40))