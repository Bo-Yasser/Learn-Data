secretAnswer = "Cairo"

answer = "" 
count = 0
limit = 3
lose = False

while secretAnswer != answer and not lose :
    
    if count < limit :
        answer = input("What Is Capital Of Egypt : ").capitalize()
    
        count += 1

    else:
        lose = True     
      
    


if lose:
    print("You Lose")  

else: 
    print("You Win") 