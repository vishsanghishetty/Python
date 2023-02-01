from random import *

random_number = randint(1, 10)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 10")
print(f"Psst the correct number is {random_number}")

user_choice = input("Choose a difficulty type 'easy' or 'hard': ")


def user():
    return int(input("Make a guess : "))


def guessing_game(max_attempts=5, msg_for_hit="You got it correct!", attempts_done_msg="Sorry you are done with your attempts"):
    for attempts in range(1, max_attempts + 1):
        user_input = user()
        if user_input == random_number:
            return msg_for_hit, attempts
        else:
            attempts_left = max_attempts - attempts
            if attempts_left == 0:
                return attempts_done_msg, max_attempts
            print(f"You have {attempts_left} attempts left, try again")


if user_choice == 'easy':
    msg, attemptsRet = guessing_game(max_attempts=3, msg_for_hit="You hit it! But is was Easy one", attempts_done_msg="get out. you could not get even do the easy one")
    print(msg, " in attempts:", attemptsRet)
elif user_choice == 'hard':
    print("hard")
    msg, attemptsRet = guessing_game(max_attempts=5, msg_for_hit="You hit it! But is was Hard one", attempts_done_msg="get out. you could not get  the Hard one")
    print(msg, " in attempts:", attemptsRet)
else:
    exit()
