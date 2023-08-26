def biggest_odd(input_numbers):
    odd_numbers = [int(num) for num in input_numbers if int(num) % 2 != 0]
    return max(odd_numbers) if odd_numbers else -1

def zeros_last(input_numbers):
    sorted_numbers = sorted(input_numbers)
    if 0 not in sorted_numbers:
        return sorted_numbers
    
    for element in range(len(input_numbers)):
        if sorted_numbers[element] == 0:
            sorted_numbers.insert(0, 0)
            del sorted_numbers[element]
    return sorted_numbers


input_list = input("Please enter some integers with no spaces between them : ")
print(f"The biggest, odd, number in your list is : {biggest_odd(input_list)}.")

numbers_list1 = [1, 4, 6, 0, 7, 0, 9]
numbers_list2 = [2, 1, 4, 7, 6]
print(f"\nThe list {numbers_list1} sorted with any zeros at the end is : {zeros_last(numbers_list1)}.")
print(f"The list {numbers_list2} sorted with any zeros at the end is : {zeros_last(numbers_list2)}.")