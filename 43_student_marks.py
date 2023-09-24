def student_marks():
    assessment_marks = {}
    complete = ''
    while complete != 'done':
        student = input("Enter the student name : ")
        mark = input("Enter {student}'s grade : ")
        complete = input("Enter done to end or enter return to add a new mark : ")
        assessment_marks.update({student: mark})
    print(assessment_marks)

student_marks()