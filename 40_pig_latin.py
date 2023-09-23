def translate(message):
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    pig_latin = [] #a list of the translated words

    for word in message.split():
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue
        
        #separate the non-letterds at the end of this word
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]

        #remember if the word was in upper or title case
        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower() # make the word lower for translation
        
        #seperate to consonants at the start of the word
        prefix_consonants =""
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]
            
        #add the pig latin ending to the word
        if prefix_consonants != "":
            word += prefix_consonants + "ay"
        else:
            word += "yay"
        
        #set the word back to original case
        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()
            
        #add the non-letters back to the start or the end of the word
        pig_latin.append(prefix_non_letters + word + suffix_non_letters)
        
    return " ".join(pig_latin)

input_message = input("Enter the english message to be translated to pig latin: ")
print(f"The Pig Latin translation of your phrase is : {translate(input_message)}.")

