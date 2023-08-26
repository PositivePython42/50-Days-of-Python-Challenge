from collections import Counter

def equal_strings(string1, string2):
    if Counter(string1) == Counter(string2):
        print("Your strings have the same length and characters.")
    elif len(string1) == len(string2) and Counter(string1) != Counter(string2):
        print("Yours strings are the same length, but have different characters in them.")
    else:
        print("Your strings have different characters in them and are different lengths.")
        
def swap_values(input_list):
    first_value = input_list[0]
    last_value = input_list[-1]
    input_list[0] = last_value
    input_list[-1] = first_value
    return input_list
    

string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ")
equal_strings(string1, string2)

print(f"Your input list is [2, 4, 67, 7] and the output is {swap_values([2, 4, 67, 7])}.")