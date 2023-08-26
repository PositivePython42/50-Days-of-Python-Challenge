def count_words(input_string):
    return len(input_string.split())

def count_elements(input_string):
    phrase = input_string.strip()
    return len(phrase)

text = input("Enter your phrase for analysis : ")
print(f"Your phrase has {count_words(text)} words and {count_elements(text)} elements.")