#I have set this up as a write file, so each time you use it it will overwrite the previous file.

def save_emails():
    email_input = ""
    email_list = []
    while email_input != "done":
        email_input = input("Enter the next email, or done if you are finished : ")
        if email_input != "done":
            email_list.append(email_input)
        
    email_file =  open("emails.txt", "w", encoding='utf-8')
    for email in email_list:
        email_file.write(email+"\n")
    email_file.close()
    
save_emails()