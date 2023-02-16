student_heights = input("Input a list of student heights\n:").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

count = 0
sum = 0
for i in student_heights:
    sum += i
    count += 1

average = round(sum / count)
print(f"The Average Height of students: {average}")

