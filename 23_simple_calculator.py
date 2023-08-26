def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

while True:
    try:
        print("Options:")
        print("Enter '+' for addition")
        print("Enter '-' for subtraction")
        print("Enter '*' for multiplication")
        print("Enter '/' for division")
        print("Enter 'q' to end the program")
        
        user_input = input(": ")

        if user_input == "q":
            break
        elif user_input in ["+", "-", "*", "/"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if user_input == "+":
                result = add(num1, num2)
            elif user_input == "-":
                result = subtract(num1, num2)
            elif user_input == "*":
                result = multiply(num1, num2)
            elif user_input == "/":
                result = divide(num1, num2)
            
            print("Result:", result)
        else:
            print("Invalid input. Please enter a valid operation.")

    except ZeroDivisionError as zde:
        print("Error:", zde)
    except ValueError as ve:
        print("Error:", ve)
    except NameError as ne:
        print("Error:", ne)
    except Exception as e:
        print("An error occurred:", e)
