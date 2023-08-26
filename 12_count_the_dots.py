import datetime

def count_dots(input_string):
    return input_string.count('.')

def age_in_minutes(user_yob):
    now = datetime.datetime.now()
    then = datetime.datetime((int(user_yob)), 1, 1)
    difference = now - then
    minutes = difference.total_seconds() / 60
    return minutes

user_string = input("Enter a string with dots in : ")
print(f"Your string has {count_dots(user_string)} full stops in it.")

valid_year = False
while valid_year is False:
    yob = input("\nEnter your year of birth in the format yyyy (years before 1900 aren't valid : ")
    if len(yob) != 4:
        print("You need to use 4 integers please.")
    if int(yob) > 1899 and len(yob) == 4:
        print(f"Your age in minutes is {age_in_minutes(yob)} minutes.")
        valid_year = True
