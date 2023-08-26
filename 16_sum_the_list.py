def sum_the_list(integer_list):
    total = 0
    for list in integer_list:
        for number in list:
            total += number
    return total

def unpack_a_nest(input_list, checklist):
    checked_list = []
    for element in input_list:
        for number in element:
            if number in checklist:
                checked_list.append(number)
    final_list = list(set(checked_list))
    return final_list

nested_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(f"Your nested list is {nested_list}, and the total of the integers in it is {sum_the_list(nested_list)}.")

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
check_list = [34, 67, 78]
print(f"Your next nested list is {nested_list}, the output list is {unpack_a_nest(nested_list, check_list)}.")

