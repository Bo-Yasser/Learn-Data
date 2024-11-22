

# 1 
'''
values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):    # all(my_list[:4]) only True

  print("Good")

else:

  print("Bad")


# output Good  '''





# 2


'''
#my_range = list(range(v))

#print(sum(my_range, v) + pow(v, v, v))  # v / v % v like >> 2 * 2 % 2 = 0


for n in range(1,821):

    if sum(list(range(n)), n) == 820:

        print(n)


# output = 40

print(sum(list(range(40)), 40) + pow(40, 40, 40))        
'''




# 3

'''
# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):



for r in range(1, 100):

    if round(sum(list(range(r))) / r) == 10 :

        print(r)




# output = 20, 21, 22        
print("#" * 50)

print(round(sum(list(range(20))) / 20))
print(round(sum(list(range(21))) / 21))
print(round(sum(list(range(22))) / 22))
'''






# 4

'''
def my_all(value):

    k = 0 

    for v in value :

        if bool(v) :

            k += 1


    if k == len(value):

        return True
    
    else:

        return False

#print(my_all([1, 2, 3])) # True
#print(my_all([1, 2, 3, []])) # False

def my_any(value):

    k = 0

    for v in value :

        if bool(v) :

            k +=1

    if k > 0 :

        return True

    else:

        return False      
    
#print(my_any([0, 1, [], False])) # True
#print(my_any([(), 0, False])) # False


def my_min(minimum):

    k = minimum[0]

    for m in minimum :

        if m < k :

            k = m

    return k 


#print(my_min([10, 100, -20, 50])) # -100
#print(my_min((10, 100, -20, -100, 50))) # -100


def my_max(maximum):

    k = maximum[0]

    for m in maximum:

        if m > k :

            k = m 

    return k

print(my_max([10, 100, -20, -100, 50])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700
'''





# 5 
'''
def remove_chars(name):
     
    return name

        
    


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)


for clean in cleaned_list :

    print(clean[1:-1])


print("#" * 50)

for n in filter(lambda name : name ,  friends_map) :

    print(n[1:-1])

'''




# 6

'''
def get_names(name) :

    
    return name.endswith("m")

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names, friends_filter)


for n in names :

    print(n)

print("#" * 50)

for n in filter(lambda name : name.endswith("m") ,  friends_filter) :

    print(n)


'''
# 7
'''
nums = [2, 4, 6, 2]
def multi(num):
    s = 0
    k = num[0]
    for m in num[1:] :
        
        k *= m

    return k

from functools import *

def multiMap(num1, num2):
    
    return num1 * num2


result = reduce(multiMap, nums)

result2 = reduce(lambda num1, num2: num1 * num2, nums)

print(multi(nums))

print(result)
print(result2)

'''   



# 8


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
    
skillsRating = enumerate(reversed(skills), 50)  
for counter, skill in skillsRating:

    if  skill in [10, 20]:

        continue
    
    print(f"{counter} - {skill}")    





