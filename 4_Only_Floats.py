def only_floats(number_one, number_two):
    if isinstance(number_one, float) and isinstance(number_two, float):
        return "2"
    elif isinstance(number_one, float) or isinstance(number_two, float):
        return "1"
    else:
        return "0"

def word_index(word_list):
    longest_wordlength = -1
    count = 0    
    
    for word in word_list:
        if len(word) > longest_wordlength:
            longest_wordlength = len(word)
            index_return = count
            count += 1

    return index_return

first = 12.1
second = 23
print(f"The function returns {only_floats(first, second)}, thank you.")

words1 = ["Hate", "remorse", "vengence"]
words2 = ["Love", "Hate"]

print(f"The first list returns {word_index(words1)}.")
print(f"The second list returns {word_index(words2)}.")
