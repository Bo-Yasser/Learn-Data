# s = input("Enter Your Name =>")
# print("Hello,", s)



#2



# c = input().split()
# print(int(c[0]) + int(c[1]) + c[2] + float(c[3]) + float(c[4]), sep="\n")


n = int(input())
x = 0
for i in range(0,n):
    k = input()
    if k.count("1") >= 2:
        x +=1
    

print(x)        


