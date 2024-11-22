


the_file = None

the_tries = 5


while the_tries > 0 :

    try: # try To Open File

        print("Enter The File Name With Absolute Path To Open")
    
        print(f"You Have {the_tries} Tries Left.")
    
        print("Example: h:/Python/Files/yourFile.extension")

        file_name_and_path = input("File Name =>  : ").strip()

        the_file = open(fr"{file_name_and_path}", "r")

        print(the_file.read())

        break

    except FileNotFoundError:

        print("File Not Found Please Be Sure the Name Is Valid")
        print()


        the_tries -= 1


    except:

        print("Error happens")
        print() 
        the_tries -= 1   
    
    finally:
        if the_file is not None :
            
            the_file.close()

            print("File Closed.")


else:

    print("All Tries Is Done")