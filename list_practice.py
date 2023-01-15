import random

names_string = input("Enter all the names separated by a comma `,` \n")

names_list = names_string.split(',')

print(f"Your entered is {names_list}")

names_list_length = len(names_list)
print(names_list_length)
random_choice = names_list[random.randint(0, names_list_length-1)]
print(f"{random_choice} is going to buy the meal today!")

print(f"{random.choice(names_list)} is going to buy the meal today!")
