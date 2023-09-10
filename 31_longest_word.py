def longest_word(input_list):
    output_word = []
    word_length = 0
    for word in input_list:
        next_word_length = len(word)
        if next_word_length > word_length:
            output_word = [next_word_length, word]
            word_length = next_word_length
    return output_word

def create_user(input_name, input_age, input_password):
    user_credentials = {"name": input_name, "age": input_age, "password": input_password}
    print("User saved.  Please login.")
    logon_name = ""
    logon_password = ""
    
    while logon_name != user_credentials["name"] or logon_password != user_credentials["password"]:
        logon_name = input("Enter your name : ")
        logon_password = input(f"Enter your password {name} : ")
        if logon_name != user_credentials["name"] or logon_password != user_credentials["password"]:
            print("Wrong password or user name, please try again.") 
        continue
    
    print("Logged in succesfully.")

        
        
word_list = ['Java', 'JavaScript', 'Python']
print(f"From {word_list}, the longest word and its length is {longest_word(word_list)}.")


print("Hello my name is Hal......")
name = input("Enter your name : ")
age = input(f"{name} enter your age : ")
password = input(f"Enter your password {name} : ")

create_user(name, age, password)


