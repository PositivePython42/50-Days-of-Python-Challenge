def most_repeated_name(name_list):
    return max(name_list, key=name_list.count)

def sorted_names(input_list):
    swapped_list = []
    for element in input_list:
        temp_name = ' '.join(reversed(element.split(' ')))
        swapped_list.append(temp_name)
    return sorted(swapped_list)

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(f"The most repeated name is {most_repeated_name(name)}.")

student_list = ["Beyoncé Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]
print(f"\nYour sorted student list is : {sorted_names(student_list)}.")