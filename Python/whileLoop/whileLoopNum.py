
numw = int(input("Enter Number Please : ").strip())

if numw == 0 :
    
    print("Number 0 Is Not Larger Than 0")

else : 

    sum = 0
    while numw > 1 : #0 :

        numw -= 1
        
        if numw == 6 :
            continue
        
        #if numw == 0 :
            #break

        print(numw)
        sum +=1


print(f"{sum} Numbers Printed Successfully.")
