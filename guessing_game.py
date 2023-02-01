from random import *

random_number = randint(1, 10)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 10")
print(f"Psst the correct number is {random_number}")

user_choice = input("Choose a difficulty type 'easy' or 'hard': ")


def user():
    return int(input("Make a guess : "))


def easy():
    max_attempts = 3
    # attempts = 0
    for attempts in range(max_attempts+1):
        user_input = user()
        if user_input == random_number:
            print("You got it correct!")
            break
        else:
            # attempts = attempts + 1
            attempts_left = max_attempts - attempts
            print(f"You have {attempts_left} attempts left, try again")

    # while not is_correct:
    #     if user_input == random_number:
    #         print("You got it correct!")
    #         break
    #
    #     else:
    #         attempts_left = number_of_attempts - 1
    #         print(f"You have {attempts_left} attempts left")
    #         user_input = user()
    #         if attempts_left == 0:
    #             break


if user_choice == 'easy':
    easy()
elif user_choice == 'hard':
    print("hard")
else:
    exit()
