



n = int(input())

for i in range(0, n):
    x = str(input())
    l = len(x)

    if l > 10 :
        print(f"{x[0]}{l-2}{x[-1]}")
    else:
        print(x)
