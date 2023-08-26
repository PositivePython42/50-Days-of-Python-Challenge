def flat_list(input_list):
    flat_list = [item for sublist in input_list for item in sublist]
    return flat_list

def your_salary(teacher_name, periods_taught, normal_rate, overtime_rate):
    if periods_taught > 100:
        overtime_paid = (periods_taught - 100) * overtime_rate
        normaltime_paid = periods_taught * normal_rate
        gross_salary = overtime_paid + normaltime_paid
    else:
        gross_salary = periods_taught * normal_rate
        
    print(f"\nTeacher: {teacher_name}\nPeriods: {periods_taught}\nGross Salary: {gross_salary:,d}")
    

nested_list = [[1, 3, 7], [2, 4, 5, 6]]
print(f"Your nested list is{nested_list} and your flattened list is {flat_list(nested_list)}.")

print()
rate = 20
extra_rate = 25
name = input("Enter the teacher's name : ")
teaching_time = int(input("Enter the number of periods taught this month : "))
your_salary(name, teaching_time, rate, extra_rate)