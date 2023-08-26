def my_discount(input_price, input_discount):
    return input_price - (input_price * (input_discount/100))

price = float(input("Please input the starting price of the product : "))
discount = float(input("Please input the discount on offer : "))
print(f"You are going to pay {my_discount(price, discount)}.")

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
Males, Females = 0, 0

for student in students:
    
    if student == 'Male' or student == 'male':
        Males +=1
    elif student == 'Female' or student == 'female':
        Females +=1
    
    student_gender = [('Male', Males), ('female', Females)]

print(student_gender)