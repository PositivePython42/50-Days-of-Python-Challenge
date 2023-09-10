import re

def password_validator(input_password):
    valid_password = re.search("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[a-zA-Z0-9]{8,1000}$", input_password)
    return valid_password

def email_validator(input_emails):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$"
    valid_emails = []
    for email in input_emails:
        if re.match(email_regex, email):
            valid_emails.append(email)
    if len(valid_emails) == 0:
        print("There are no valid emails.")
    else:
        print(f"From the emails supplied, these {valid_emails} are valid.")

while True:
    password = input("Enter a valid password : ")
    if password_validator(password) is not None:
        print(f"Your password {password} is valid.")
        break
    else:
        continue
    
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
email_validator(emails)