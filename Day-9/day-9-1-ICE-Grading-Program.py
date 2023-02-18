student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for thing in student_scores:
    x = student_scores[thing]
    if x > 90 and x < 101:
        student_grades[thing] = "Outstanding"
    elif x > 80 and x < 91:
        student_grades[thing] = "Exceeds Expections"
    elif x > 70 and x < 81:
        student_grades[thing] = "Acceptable"
    elif x <= 70:
        student_grades[thing] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)