def capitalize(phrase):
    return phrase.title()

def reversed_list(input_string):
    list_of_words = list(input_string.split())
    words_with_caps = []
    for word in list_of_words:
        for letter in word:
            if letter.isupper():
                reversed_word = word[::-1]
                words_with_caps.append(reversed_word)
    return words_with_caps   


user_phrase = input("Enter your phrase and I'll capitalise it for you : ")
print(f"Your phrase, capitaised is {capitalize(user_phrase)}.")

str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
print(f"The list of words with caps in and reversed are {reversed_list(str1)}.")