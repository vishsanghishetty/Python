name_first_person = input("Enter the first person's name\n").lower()
name_second_person = input("Enter the second person's name\n").lower()

combined_string_lower = (name_first_person + name_second_person).lower()
print(combined_string_lower)

true = combined_string_lower.count("t") + combined_string_lower.count("r") + combined_string_lower.count("u")\
       + combined_string_lower.count("e")

love = combined_string_lower.count("l") + combined_string_lower.count("o") + combined_string_lower.count("v")\
       + combined_string_lower.count("e")

print(true)
print(love)
score = str(true) + str(love)
print(score)

love_score = int(score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")

elif 50 < love_score < 90:
    print(f"Your score is {love_score}, you are alright together")

else:
    print(f"Your score is {love_score}")


#  = combined_string_lower.count("r")
# t = combined_string_lower.count("u")
# t = combined_string_lower.count("e")




#PEMDAS -> Left to Right
#BMI
# weight = int(input("Enter weight \n"))
# height = float(input("Enter height \n"))
#
# # wint = int(weight)
# # hint = float(height) * float(height)
#
# bmi = round(weight/height ** 2)
# if bmi < 18.5:
#     print(f'{bmi} : is your BMI, you are underweight')
#
# elif bmi < 25:
#     print(f'{bmi}: is your BMI, you have normal weight')
#
# elif bmi < 30:
#     print(f'{bmi} : is your BMI, you are over weight')
#
# elif bmi < 35:
#     print(f'{bmi}: is your BMI, you are obese')
#
# else:
#     print(f'{bmi}: is your BMI, you are clinically obese')

#####
# print(str(int(bmi)) + " : is your BMI")
# print(f'{str(round(bmi))} : is your BMI')

# round - rounds of the nearest number
# 8 //3 - returns integer, chops of all the decimal numbers
















# checks a number if it odd or even

# number = int(input("Enter a number\n"))
#
# if number % 2 == 0:
#     print(f'{number} % 2 == 0, so {number} is even')
#
# else:
#     print(f"{number} is an odd number")


