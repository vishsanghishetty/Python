from random import randint

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty - easy or hard : ")


def set_difficulty():
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        exit()


def check(guess, random_answer, turns):
    if guess > random_answer:
        print("Too high")
        return turns - 1
    elif guess < random_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it correct!")


def game():
    random_answer = randint(1, 100)
    print(f"Psst answer is {random_answer}.")
    guess = 0
    turns = set_difficulty()
    while guess != random_answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        turns = check(guess, random_answer, turns)
        if turns == 0:
            print("You ran out of guesses, you LOSE!")
            return
        elif guess != random_answer:
            print("Guess again")


game()
