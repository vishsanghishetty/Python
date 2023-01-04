current_age = int(input("Age"))
expected_age_to_live = 90 - current_age

print(f"You have {expected_age_to_live * 365} days, {expected_age_to_live * 52} weeks, and {expected_age_to_live * 12} months to live")

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months





#print("Hey there" + input("what is your name?"))
# name = input("what is your name?")
#print(len(name))
#
# print(len(name))
#
# x = input("x: ")
# y = input("y: ")
#
# a = x
# x = y
# y = a

# print(x + ": x")
# print(y + ": y")

#1
print("Hello folks!")

#2
city = input("Enter the city you were born in? \n")

#3
pet_name = input("Enter the name of your pet \n")

#4
print("Your band name is : " + city + " " + pet_name)


number = input("Enter a 2 digit number")
num1 = number[0]
num2 = number[1]

print(type(num1), type(num2))

print(int(num1) + int(num2))

#PEMDAS -> Left to Right
#BMI
weight = int(input("Enter weight \n"))
height = float(input("Enter height \n"))

# wint = int(weight)
# hint = float(height) * float(height)

bmi = weight / height ** 2

print(str(int(bmi)) + " : is your BMI")


# round - rounds of the nearest number
# 8 //3 - returns interger, chops of all the decimal numbers

#f-String

print(f"Your BMI is : {int(bmi)}")


