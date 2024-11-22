import os 

#print(os.getcwd())


#my_file = open(r"h:/Python/Files/osama.txt", "r")

########## r ##########

# 1

#print(my_file)        
#print(my_file.name)        
#print(my_file.mode)        
#print(my_file.encoding)   

# 2

# print(my_file.read())
# print(my_file.read(5))

# 3

#print(my_file.readline(10))
#print(my_file.readline())


# 4

#print(my_file.readlines())
#print(my_file.readlines(50))

#print(type(my_file.readlines()))



#for line in my_file :

    #print(line)

    #if line.startswith("7"):

        #break


#my_file.close() 
   


#--------------------------------

########## w ##########

# 1


#my_file = open(r"h:/Python/Files/osama.txt", "w")

#my_file.write("Hello From Python With Love\n")

#my_file.write("Hello\n")

#my_file.write("Second Line")

#my_file.write("Third Line")



# 2

#myList = ["Osama\n", "Ahmed\n", "Sayed\n"]

#my_file = open(r"h:/Python/Files/osama.txt", "w")

#my_file.writelines(myList)




#--------------------------------


########## a ##########


# 1


#my_file = open(r"h:/Python/Files/osama.txt", "a")

#my_file.write("Elzero")



# 2 

#myList = ["Osama\n", "Ahmed\n", "Sayed\n"]

#my_file.writelines(myList)




#--------------------------------



########## syntax ##########

# 1 .truncate()


#my_file = open(r"h:/Python/Files/osama.txt", "r")


# my_file.truncate(5)

# print(my_file.tell())




#my_file.seek(6)

#print(my_file.tell())

#print(my_file.read())


# os.remove(r"h:/Python/Files/osama.txt")



