def same_in_reverse(entered_string):
    reversed_string = entered_string[::-1]
    return entered_string == reversed_string

def your_age(search_name):
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    search = search_name.lower()
    if search in names_age:
        print(f"{search_name}'s age is {names_age[search]}")
    else:
        new_name_age = int(input(f"Enter {search_name}'s age : "))
        names_age.update({search_name.lower(): new_name_age})
        print(f"The new dictionary is {names_age}")

string = input("Enter a string and I will test if it is the same when reversed : ")
if same_in_reverse(string):
    print(f"Your string {string} is the same forwards and backwards!")
else:
    print("Try again")

search_term = input("Enter a name to search : ")
your_age(search_term)

