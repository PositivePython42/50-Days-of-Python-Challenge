def any_number(input_list):
    return sum(input_list) / len(input_list)

def add_reverse(first_list, second_list):
    summed_list = []
    for calculation in range(len(first_list)):
        summed = first_list[calculation] + second_list[calculation]
        summed_list.append(summed)
    return summed_list[::-1]

list_of_numbers = []
while True:
    add_to_list = input("Type an integer or float for your list, enter q to get the average of your list : ")
    if add_to_list == 'q' :
        break
    else:
        list_of_numbers.append(float(add_to_list))        
print(f"The average of {list_of_numbers} is {any_number(list_of_numbers)}.")

list1, list2 = [10, 12, 34], [12, 56, 78]
print(f"\n\nThe lists are {list1} and {list2}.")
if len(list1) != len(list2):
    print("The lists or not of equal lengths.")
else:
    print(f"The list created by adding each same indexed number and reversing the order is {add_reverse(list1, list2)}.")