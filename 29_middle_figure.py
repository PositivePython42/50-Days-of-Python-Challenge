import math

def middle_figure(first_string, second_string):
    joined = first_string+second_string
    joined.strip()
    if joined == "":
        return "NO MIDDLE FIGURE"
    elif len(joined) % 2 == 0:
        return "NO MIDDLE FIGURE"
    else:
        return joined[math.floor(len(joined)/2)]

a = input("Enter your first string : ")
b = input("Enter your second string : ")
print(f"The middle character of the two strings you entered is {middle_figure(a, b)}.")