def index_position(input_string):
    indexes = []
    for element in range(0, len(input_string)):
        if input_string[element].islower():
            indexes.append(element)
    return indexes

def largest_number(input_list):
    new_number_list = []
    next_list = []
    
    for item in input_list:
        temp = ''.join(sorted(str(item), reverse=True))
        next_list.append(temp)
    
    for element in range(9, 1, -1):
        for item in next_list: 
            if int(str(item)[0]) == element:
                new_number_list.append(item)
    
    new_number_string = ""
    for i in new_number_list:
        new_number_string += str(i)
    
    return int(new_number_string)
        


entry_string = input("Enter a single string with a mixture of lower and UPPER case letters : ")
print(f"The index positions of the lower case letters are : {index_position(entry_string)}.")


list1 = [3, 67, 87, 9, 2]
print(f"\n\nThe largest number you can make by rearranging these integers is {largest_number(list1):,d}.")
