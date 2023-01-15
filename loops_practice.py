student_heights = [125, 234, 452, 129, 199, 100]

# average_height = sum(student_heights) / len(student_heights)
#
# print(f"Average height of a student is {average_height}")

sum_of_heights = 0
for student_height in student_heights:
    sum_of_heights = sum_of_heights + student_height
print(sum_of_heights)
print(f"Average height of a student is {sum_of_heights/len(student_heights)}")