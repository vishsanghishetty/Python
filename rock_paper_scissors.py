import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
game_list = [rock, paper, scissors]

print(f"User chose {user_input}\n")
print(f"{game_list[user_input]} \n")
computer_choice = random.choice(game_list)
print(f"Computer chose {game_list.index(computer_choice)} \n")
print(computer_choice)

if user_input == 0 and game_list.index(computer_choice) == 2:
    print(f"You win, Rock beats Scissors")
elif user_input == 1 and game_list.index(computer_choice) == 0:
    print(f"You win, Paper beats Rock")
elif user_input == 2 and game_list.index(computer_choice) == 1:
    print(f"You win, Scissors beats Paper")
elif user_input == 2 and game_list.index(computer_choice) == 0:
    print(f"You lose, Rock beats Scissors")
elif user_input == 1 and game_list.index(computer_choice) == 2:
    print(f"You lose, Scissors beats Paper")
elif user_input == 0 and game_list.index(computer_choice) == 1:
    print(f"You lose, Paper beats Rock")

elif user_input == game_list.index(computer_choice):
    print("It's a draw")











# if user_input == 0:
#     print(f" You chose {user_input} {rock}")
# elif user_input == 1:
#     print(f" You chose {user_input} {paper}")
# elif user_input == 2:
#     print(f" You chose {user_input} {scissors}")
#
# choice_list = [rock, paper, scissors]
# random_choice = random.choice(choice_list)
#
# print(f"Computer chose {choice_list.index(random_choice)}")
#
# if user_input == 0 and random_choice == choice_list[2]:
#     print("You win \n")
#     print("Rock wins against scissors")
# elif user_input == 2 and random_choice == choice_list[1]:
#     print("You win \n")
#     print("Scissors win against paper")
# elif user_input == 1 and random_choice == choice_list[0]:
#     print("You win \n")
#     print("Paper wins against rock")
# else:
#     print("It's a Draw!!")
