first = ["⭐", "⭐", "⭐"]
second = ["⭐", "⭐", "⭐"]
third = ["⭐", "⭐", "⭐"]

treasure_map = [first, second, third]
print(f"    1      2      3")
print(f"1 {first} \n2 {second} \n3 {third}")

print(treasure_map[2][1])
treasure_position = input("where do you want to place your treasure? \n")

horizontal = int(treasure_position[0])
vertical = int(treasure_position[1])

treasure_map[vertical-1][horizontal-1] = "😊"


print(f"1 {first} \n2 {second} \n3 {third}")
