days = 1
calorie_list = []
nested_list =[]

def average_calories(list):
    return sum(list) / len(list)

def nest_lists(*argv):
    for arg in argv:
        nested_list.append(arg)
    return nested_list

print("Calorie Calc, when you are done inputting daily values, input 0 to get your average.")

while True:
    daily_calories = int(input(f"How any calories consumed on day {days} : "))
    if daily_calories == 0 and days == 1:
        print("You have to enter at least 1 value")
        continue
    if daily_calories == 0:
        print(f"Your average intake has been {average_calories(calorie_list)} calories.")
        break
    else:
        calorie_list.append(daily_calories)
        days += 1

list1, list2, list3 = [1, 2, 3, 5], [1, 2, 3,4], [1, 3, 4, 5]
print(f"Your nested lists are {nest_lists(list1, list2, list3)}.")