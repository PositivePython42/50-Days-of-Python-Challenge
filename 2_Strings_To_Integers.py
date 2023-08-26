import collections

list_of_strings = ["1", "3", "5"]
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def convert_add(string_of_numbers):
    
    total = 0
    list_of_integers = []
    
    for string in string_of_numbers:
        list_of_integers.append(int(string))
        total += int(string)
        
    print(f"The list of integers is {list_of_integers} and their sum is {total}.")
    
def check_duplicates(string_of_words):
    if len(string_of_words) == len(set(string_of_words)):
        print("There are no duplicates in your list")
    else:
        print([item for item, count in collections.Counter(string_of_words).items() if count > 1])

convert_add(list_of_strings)
check_duplicates(fruits)
check_duplicates(names)