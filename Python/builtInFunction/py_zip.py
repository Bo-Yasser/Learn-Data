



list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]

tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {
    "Name": "Osama",
    "Age": 36,
    "Country": "Egypt",
    "Skill" : "Python"
}



# for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

#     print("List 1 Item =>", item1)
#     print("List 2 Item =>", item2)
#     print("Tuple 1 Item =>", item3)
#     print("Dict 1 Key =>", item4, "Value =>", dict1[item4])




# ultimateList = zip(list1, list2)

# print(ultimateList)

# for item in ultimateList:

#     print(item)




#################### zip Practice ####################


# 1

# my_lis1 = ["E", "Z", "R", 1, 2, 3]
# my_tuple1 = ("L", "E", "O")
# my_data1 = []

# for data in zip(my_list1, my_tuple1):
  
#   my_data1.extend(data)

#   final_String1 = "".join(my_data1).capitalize()


# print(final_String1) # Elzero


# 2

my_list2 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple2 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_tuple3 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data2 = []

for item1, item2, item3 in zip(my_list2, my_tuple2, my_tuple3):
    
    if item1 in [1, 2] :

        continue
    
    
    my_data2.append(item1)

    final_string2 = "".join(my_data2).capitalize()


print(final_string2)


    

   


