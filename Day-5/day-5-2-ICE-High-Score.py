student_scores = input("Input list of student scores\n:").split()

for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(f"The Score List: {student_scores}")

max = 0
min = student_scores[0]

for score in student_scores:
    if score > max:
        max = score
    if score < min:
        min = score

print(f"The Highest Score is: {max} And \nThe Lowest Score is: {min}")



