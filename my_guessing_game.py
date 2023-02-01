from random import randint

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty - easy or hard : ")
random_num = randint(1, 100)
print(f"Psst answer is {random_num}")


# def guessing_game(level, max_attempts, success_msg="You got it correct",
#                   attempts_done_msg="You are done with attempts"):
#     for i in range(1, max_attempts + 1):
#         user_num = int(input("Make a guess : "))
#         if random_num == user_num:
#             return success_msg, i
#         else:
#             attempts_left = max_attempts - i
#             if attempts_left == 0:
#                 return attempts_done_msg, i
#             print(f"You have {attempts_left} attempts left, try again")

def guessing_game(difficulty, max_attempts):
    for i in range(1, max_attempts + 1):
        k = max_attempts + 1 - i
        print(f"You have {k} attempts to guess the number")
        user_num = int(input("Make a guess : "))
        if user_num == random_num:
            return f"You got it correct in {i} attempts in {difficulty} level"
        else:
            attempts_left = max_attempts - i
            if attempts_left == 0:
                return f"You have exhausted all the {max_attempts} attempts"
        # print(f"Guess again, you have {attempts_left} attempts left")


if level == 'easy':
    EASY_LEVEL_ATTEMPTS = 3
    msg = guessing_game(level, EASY_LEVEL_ATTEMPTS)
    print(f"{msg}")
elif level == 'hard':
    HARD_LEVEL_ATTEMPTS = 5
    msg = guessing_game(level, HARD_LEVEL_ATTEMPTS)
    print(f"{msg}")
else:
    exit()
