import string

def check_panagram(check_list, check_phrase):
    return all([element in check_phrase for element in check_list])

def find_index(search_for, input_list):
    index_list = []
    for element in range(len(input_list)):
        if input_list[element] == search_for:
            index_list.append(element)
    if index_list:
        return index_list
    else:
        return [search_for, search_for, search_for, search_for, search_for, search_for]
        
alphabet = list(string.ascii_lowercase)
phrase = input("Enter the phrase you want me to check if it is a Panagram : ")

print(f"It is {check_panagram(alphabet, phrase)} that your phrase is a Panagram.")

number_list = [1, 2, 4, 6, 7, 7]
search_number = 7
print(f"{search_number} is at indexes {find_index(search_number, number_list)}.")

number_list = [1, 2, 4, 6, 7, 7]
search_number = 8
print(f"{search_number} is an indexes {find_index(search_number, number_list)}.")

