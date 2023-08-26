def register_check(todays_register):
    attendance = 0
    
    for student in todays_register.values():
        if student == 'yes':
            attendance += 1
        else:
            continue
        
    return attendance

def filter_sort_names(name_list):
    names_for_register = []
    
    for name in name_list:
        if name.lower() == name:
            names_for_register.append(name)
        else:
            continue
        
    return tuple(names_for_register)

register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
print(f"There are {register_check(register)} students in school today.")

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(f"The names in lower case, sorted alphabetically are {filter_sort_names(names)}.")
