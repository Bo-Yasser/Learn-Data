# 1
'''a = 0
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)

for num in my_nums :
    
    if num % 5 == 0 :
       
       a += 1  
       
       print(f"{a} => {num}")

print('All Numpers Printed')       '''


# 2

'''for num in range(1,21) :

    if num in [6, 8, 11]:

        continue
     
    print(f"\"{str(num).zfill(2)}\"")



else: 
    print("All Numbers Printed")'''


# 3

'''my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}  


ranks = {
    "A" : 100,
    "B" : 80,
    "C" : 40
}

total = 0

for rank_key, rank_value in my_ranks.items() :

    print(f"My Rank In {rank_key} Is {rank_value} And This Equal {ranks[rank_value]} Points")

    total += ranks[rank_value]

else:
    print(f"Total Points Is {total}")'''


# 4

'''students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}



marks = {
    "A" : 100,
    "B" : 80,
    "C" : 40,
    "D" : 20
}




 


for name in students :

    
    print("-" * 50) 
    
    print(f"\"-- Student Name => {name}\"")
    
    print("-" * 50)  
    all = 0
    for book in students[name] :

        print(f"\"- {book} => {marks[students[name][book]]} Points\"")

        
       
        all += marks[students[name][book]]
    print(f"\"Total Points For {name} Is {all}\"")   

print("-" * 50)  
    



for  key, value in students.items() :


    print("-" * 50)

    print(f"\"-- Student Name => {key}\"")  

    print("-" * 50)
    
    o = 0

    for A_key, A_value in value.items() :

        print(f"\"{A_key} => {marks[A_value]} Points\"")

        o += marks[A_value]

    print(f"\"Total Points For {key} Is {o}\"")        

print("-" * 50)'''




