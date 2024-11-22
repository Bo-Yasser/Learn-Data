
# 1


import os

#file = os.path.abspath(__file__)
#file = file[::-1]
#file = file[: file.index("\\")]
#file = file[::-1]




#s = 0

#for n in range(1, 51):

    #if n == 25 :
        #folder2 = open(r"\Python\Files\PY\special-text.txt","x")
        #folder2.close()

    #else:

        #folder3 = open(fr"\Python\Files\PY\txt{n}.txt", "a")  
        #folder3.write(f"Elzero Web School => {n}\n")
        #folder3.close()

    #s += 1



#print(os.getcwd())
#print(os.path.abspath(__file__))
#print(file)
#print(s)    





# 2


#folder4 = open(r"H:\Python\Files\PY\txt1.txt","a")
#folder4.write("Appended => Elzero Web School\n" * 50)
#folder4.close()







# 3

folder5 = open(r"H:\Python\Files\PY\txt1.txt", "r")

list = folder5.readlines()

lines_num = len(list)

words_num = 0
chars_num = 0
chars_l_num = 0


for x in list :

    o = x.split()                #split make list for every part by defult with spcae " " [1, elzero, web, school] # do for all parts in  first list 

    words_num += len(o)


    for letter in x : 

        char = letter.strip()

        chars_num += len(char)

        chars_l_num += char.count("l")

print(f"Number Of Lines Is => {lines_num}")
print(f"Number Of Words Is => {words_num}")
print(f"Number Of Chars Is => {chars_num}")
print(f"Number Of \"l\" Char Is => {chars_l_num}")



#for r in range(41,51):

    #os.remove(fr"H:\Python\Files\PY\txt{r}.txt")