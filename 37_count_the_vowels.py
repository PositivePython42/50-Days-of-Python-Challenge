def count_the_vowels(input_string):
    vowels = list('aeiouAEIOU')
    count = 0
    for element in range(len(input_string)):
        if input_string[element] in vowels:
            count += 1
            vowels.remove(input_string[element])
    return count


search_string = input("Enter the string you want to search : ")
print(f"Your string has {count_the_vowels(search_string)} vowels.")