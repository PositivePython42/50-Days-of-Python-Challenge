def count(input_string):
    letter_dictionary = {}
    input_string.strip()
    letter_list = list(set(input_string))
    for element in letter_list:
        letter_count = 0
        for letter in range(len(input_string)):
            if input_string[letter] == element:
                letter_count += 1
                letter_dictionary[input_string[letter]] = letter_count
    return letter_dictionary

user_string = input("Enter the string you'd like to analyse : ")
print(f"The dictionary showing how many times each letter appears is : {count(user_string)}")