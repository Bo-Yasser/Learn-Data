myNumbers = [1,2,3,5,7,10,13,14,15,19]


#continue

for number in myNumbers :

   if number == 13 :
      
      continue
   
   print(number)

print("#"* 50)

#break

for number in myNumbers :

   if number == 13 :
      
      break
   print(number)
   

print("#"* 50)

#pass

for number in myNumbers :

   if number == 13 :
      pass
     
   print(number)
   