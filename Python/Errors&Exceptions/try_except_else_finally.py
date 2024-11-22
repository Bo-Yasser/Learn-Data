




# try:

#     number = int(input("Write Your Number: "))
#     print("Good, This Is Integer From Try")


# except:

#     print("Bad, This Is Not Integer")

# else:
#     print("Good, This Is Integer From Else")


# finally:

#     print("Print from Finally What Ever Happend")    




try:

    # print(10/0)
    # print(x)
    print(int("Hello"))

except ZeroDivisionError:

    print("Can't Divide")
except NameError:
    print("Identifier Not Found")

except ValueError:

    print("Value Error Yaser")    

except:
    print("Error Happens")    
