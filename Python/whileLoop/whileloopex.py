num = int(input("Enter Your Number : "))

if num == 0 :
    print("Number 0 Is Not Larger Than 0")


else:
    
    
    sum = 0
    while num > 1 :
       
       num -= 1
       
       if num == 6 :
          continue
    
    
       print(num)
       sum += 1


print(f"{sum} Numbers Printed Successfully.")
