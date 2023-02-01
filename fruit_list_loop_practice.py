fruit_list = ["pear", "pomegranate", "grape", "orange", "kiwi", "cherry", "mango", "banana", "apple"]

# user_input = "stop"
print("Let's play a fruit searching game")
game = "stop"

for fruit in fruit_list:
    fruit = input("Enter a fruit : ")
    if fruit in fruit_list:
        found = fruit_list.index(fruit)
        print(f"Fruit you entered is at index {found} in the list")
        break
    elif fruit not in fruit_list:
        if fruit == game:
            print("game stopped")
            break
        print(f"Try again")
