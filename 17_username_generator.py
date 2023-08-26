from random import randint

def user_name(name):
    gen_name = ""
    pos = -1
    for element in range(len(name)):
        gen_name += name[pos]
        pos -= 1
        
    gen_name = gen_name + str(randint(0,9))    
    return gen_name

def sort_length(names):
    for i in range(len(names)):
        for j in range(0, len(names) - i - 1):
            if len(names[j]) > len(names[j + 1]):
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

real_name = input("Enter your name (no spaces) here : ")
print(f"Your system user name is {user_name(real_name)}.")

names = ["Peter", "Jon", "Andrew"]
print(f"\nThe names {names} in order by length are {sort_length(names)}.")