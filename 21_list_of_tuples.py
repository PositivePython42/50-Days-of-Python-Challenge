def make_tuples(list_a, list_b):
    tuples = []
    for i in range(len(list_a)):
        tuples.append((list_a[i], list_b[i]))
    return tuples

def even_or_average():
    list_of_numbers = []
    biggest = 0
    for ele in range(5):
        number = int(input("Enter an integer : "))
        list_of_numbers.append(number)
    
    for item in range(len(list_of_numbers)):
        if list_of_numbers[item] % 2 == 0:
            if list_of_numbers[item] > biggest:
                biggest = list_of_numbers[item]
    if biggest == 0:
        return sum(list_of_numbers) / len(list_of_numbers)
    else:
        return biggest

lista, listb = [1, 2, 3, 4], [5, 6, 7, 8]
print(f"Yours lists are {lista} and {listb}, combined as a list of tuples they are {make_tuples(lista, listb)}.")

print(f"The number returned from even_or_average() is {even_or_average()}.")