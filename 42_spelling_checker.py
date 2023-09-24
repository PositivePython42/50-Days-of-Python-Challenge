from textblob import Word
import winsound
import datetime

def spelling_checker(input_word):
    checked_word = Word(input_word)
    if checked_word.correct() == input_word:
        return True
    else:
        return False
    
def alarm():
    hour =  input("\nWhat hour (24 hour clock) do you want your alarm for : ")
    minute  = input("What minute do you want you alarm for : ")
    print(f"You alarm will go off at {hour + minute}.")
    while True:
        if int(hour) == datetime.datetime.now().hour and int(minute) == datetime.datetime.now().minute:
            print("Time to get up!")
            winsound.Beep(2500, 2000)
            break 

user_word = input("Enter the word you want to spellcheck : ")

while spelling_checker(user_word) is True:
    print(f"Well done **{user_word}** is a correct spelling")
    alarm()
    exit()
    
confirm = input(f"Did you mean to enter {user_word}?")
if confirm == 'n':
    user_word = input("Try Again : ")
    spelling_checker(user_word)
elif confirm == 'y':
    print(f"Though we cannot see it, you are saying {user_word} is correct.")
    print(f"We think the word is {Word(user_word).correct()}.")
    
alarm()