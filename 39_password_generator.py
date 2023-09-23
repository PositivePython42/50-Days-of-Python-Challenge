import random, string

def generate_password(strength: str) -> int:
    if strength == 'w':
        length = 5
    elif strength == 's':
        length = 8
    elif strength == 'v':
        length = 12
    else:
        raise ValueError(f"Invalid length: {length}")

    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    return password

password_strength = input("Enter w for a weak password, s for a strong one and v for a very strong password : ")
print(f"Your password is {generate_password(password_strength)}")