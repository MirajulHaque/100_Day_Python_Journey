print("Welcome to BMI Calculator 2.0")
height = float(input("Enter your height in Meter\n:"))
weight = float(input("Enter your weight in Kilogram\n:"))
bmi = round((weight/(height * height)))

print(f"Your BMI is: {bmi}")
if bmi <18.5:
    print("Status: Underweight")
elif bmi < 25:
    print("Status: Normal Weight")
elif bmi < 30:
    print("Status: Overweight")
elif bmi < 35:
    print("Status: Obese")
else:
    print("Status: Clinically Obese")
