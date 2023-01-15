sum_of_numbers = 0
for i in range(0, 11):
    sum_of_numbers = sum_of_numbers + i
print(f"{sum_of_numbers}")


for x in range(0, 101):
    if x % 2 == 0:
        print(f"{x}")


for y in range(1, 101):
    if y % 3 == 0 and y % 5 == 0:
        print("FizzBuzz")
    elif y % 5 == 0:
        print("Buzz")
    elif y % 3 == 0:
        print("Fizz")
    else:
        print(y)

