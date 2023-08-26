def hide_password():
    user_password = input("Enter your password : ")
    new_password = len(user_password) * "*"
    print(f"Your new password is {len(new_password)} characters long and is {new_password}.")
    
def convert_numbers(n):
    new_list = []
    for num in n:
        new_list.append("{:,}".format(num))
    return new_list

hide_password()
print(convert_numbers([1000000, 2356989, 2354672, 9878098]))