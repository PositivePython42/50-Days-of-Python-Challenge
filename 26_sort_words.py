def sort_words(input_string):
    deduped_string =[]
    remove_whitespace = ''.join(input_string.split())
    for element in range(0, len(remove_whitespace)-1):
        if remove_whitespace[element] not in deduped_string:
            deduped_string.append(remove_whitespace[element])
    sorted_string = sorted(deduped_string)
    return sorted_string

def string_length(input_string):
    string_dictionary = {}
    string_list = input_string.split()
    for element in string_list:
        string_dictionary[element] = len(element)
    return string_dictionary   

string = input("Enter your string and I'll de-dupe and sort the letters : ")
print(f"\nYour deduped and sorted letters are : {sort_words(string)}.")

print(f"\nThe length of each word in your string is : {string_length(string)}")