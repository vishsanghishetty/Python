student_scores = {
    "Sumanth": 100,
    "Vishali": 85,
    "Sanihith": 99,
    "Sia": 99,
    "Dog": 50,
    "Cat": 20
}

student_grades = {}
for student in student_scores:
    if 91 < student_scores[student] <= 100:
        student_grades[student] = "Outstanding"

    elif 81 < student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"

    elif 71 < student_scores[student] <= 80:
        student_grades[student] = "Acceptable"

    elif student_scores[student] <= 70:
        student_grades[student] = "Fail"


print(student_grades)










things_to_eat = {
    "fruit": "apple",
    "vegetables": "broccoli",
    "poultry": "chicken",
    "sea-food": "fish",
    "meat": "beef"
}

for thing in things_to_eat:
    print(f"{thing} - {things_to_eat[thing]}")
    # print(things_to_eat[thing])

