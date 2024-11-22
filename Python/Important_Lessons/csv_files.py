import csv

# values in csv file separated by , #comma#


file = open(r"h:/Python/Important_Lessons/csv.csv", "a")

# get name, get number
name = input("Name: ")
number = input("Number: ")
name1 = input("Name: ")
number1 = input("Number: ")
# append data to csv file as row
writer = csv.writer(file)#.writerow()
writer.writerows([name,number])


file.close()