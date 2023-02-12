age = int(input("Enter your current age\n:"))

age_left = 90 - age
days = age_left * 365
weeks = age_left * 52
months = age_left * 12

print(f"You have {days} days, {weeks} weeks, {months} months left")
