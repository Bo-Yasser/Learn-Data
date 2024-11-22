
x = "wwwoooorrrldd"




def clean_word(word) : 
    


    if len(word.upper()) == 1 :

        return word
    
    print(f"1- Print Start Function {word}")
    

    if word[0] == word[1] : # wwwoooorrrldd

        print(f"2- Print Before Condition {word}")

        return clean_word(word[1:])
    

    print(f"3- Print Before Return {word}")

    return word[0] + clean_word(word[1:])

    # stash  [ World ]
     
print(clean_word("wwwoooorrrldd"))   


    