from random import randint
number_list= []

def unique_numbers(input_list):
    sum_input_list = sum(input_list)
    unique_number_list = list(set(input_list))
    sum_unique_list = sum(unique_number_list)
    subtraction = sum_input_list - sum_unique_list
    if subtraction % 2 == 0:
        return input_list
    else:
        return unique_number_list

def difference(lista, listb):
    return [element for element in lista if element not in listb] + [element for element in listb if element not in lista]

number_volume = input("Tell me how many random numbers between 1 and 20 you want to use : ")
for element in range(1, int(number_volume)):
    number_list.append(randint(1, 10))
print(f"Your random number list is {number_list}.")

print(f"The returned list is       {unique_numbers(number_list)}.")

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

print(f"\nYour lists are {list1} and {list2}, the items in the first, but not in the second list (and vice versa) are {difference(list1, list2)}.")