import random

def guess_a_number(target):
    turn = 1
    while turn <= 3:
        guess = int(input("Guess the number : "))
        if guess < target:
            print("Higher")
        elif guess > target:
            print("Lower")
        elif guess == target:
            print("Just right, you're a winner!")
            return  
        turn += 1
    print(f"Hard luck, loser!  The number was {target}.")
    
def missing_numbers(input_list):
    complete_set = []
    return_list = []
    low = input_list[0]
    high = input_list[-1]
    for number in range(int(low), int(high), 1):
        complete_set.append(number)
    for number in complete_set:
        if number not in input_list:
            return_list.append(number)
    return return_list

print("Generating the random number")
guess_a_number(random.randint(1, 100))

number_list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
print(f"Your list is {number_list}.  The missing numbers are {missing_numbers(number_list)}.")