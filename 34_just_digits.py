def just_digits():
    numbers_found = []
    
    with open('/home/seany42/Documents/50 Python Challenges/python.csv', 'r') as f: #when you use this  you eill need to put the filr path in for your setting
        for line in f:
            words = line.split()
            for element in words:
                if element.isnumeric(): 
                    numbers_found.append(element)
    return numbers_found

print(f"I have read your text file and the numbers in it are : {just_digits()}.")