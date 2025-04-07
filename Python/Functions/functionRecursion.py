
x = "wwwoooorrrldd"




def clean_word(word) : 
    


    if len(word) == 1 :

        return word
    
    if word[0] == word[1] : # wwwoooorrrldd

        return clean_word(word[1:])
    


    return word[0] + clean_word(word[1:])

    # stash  [ World ]
     
print(clean_word("wwwoooorrrldd"))   


   