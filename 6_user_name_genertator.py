def user_name(input_data):
    data_split = input_data.split("@")
    return data_split[0]

def zeroed(input_list):
    input_list[0] = 0
    input_list[-1] = 0
    return input_list

email_address = input("Enter your email address : ")
print(f"\nYour user name is : {user_name(email_address)}.")

code_to_zero =  [2, 5, 7, 8, 9]
print(f"\nYour zeroed code is {zeroed(code_to_zero)}.")