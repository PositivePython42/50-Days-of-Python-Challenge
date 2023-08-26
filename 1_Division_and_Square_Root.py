import math

def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5
    
the_number = int(input("Please enter your number : "))
print(f"Your result is {divide_or_square(the_number)}.")

fruits = {'fruit': 'apple', 'color': 'green', 'taste' : 'tart', 'seed': 'pip'}

def longest_value(search):
    
    value_length = 1

    for item in search.values():
        if len(item) > value_length:
            longest_item = item
            value_length = len(item)
    return longest_item

print(f'The longest word in the dictionaries values is {longest_value(fruits)}.')
