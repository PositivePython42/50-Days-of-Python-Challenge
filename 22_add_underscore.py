def add_hash(input_phrase):
    return input_phrase.replace(" ", "#")

def add_underscore(input_phrase):
    return input_phrase.replace("#", "_")

def remove_underscore(input_phrase):
    return input_phrase.replace("_", " ")

user_phrase = input("Enter your phrase : ")
print(f"Your phrase with hashes : {add_hash(user_phrase)}.")
print(f"Your phrase with underscores : {add_underscore(add_hash(user_phrase))}.")
print(f"Through all 3 functions :{(remove_underscore(add_underscore(add_hash(user_phrase))))}.")

