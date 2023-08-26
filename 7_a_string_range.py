from collections import Counter

def string_range(number_to_iterate):
    output_string = ""
    for element in range(number_to_iterate):
        output_string += str(element)
        output_string += "."
    return output_string

def dictionary_of_names(list_of_names):
    output_list = []
    for name in list_of_names:
        if name[0] == "S":
            output_list.append(name)
    return Counter(output_list)


items_for_string = int(input("Enter the amont of items you'd like in your strong : "))
print(f"\nYour exit string is...... {string_range(items_for_string)}")

names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
print(f"\n\nThe names that start with S and a count of their frequency is : {dictionary_of_names(names)}.")