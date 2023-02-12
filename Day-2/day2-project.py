print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? \n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? \n:"))
member = int(input("How many people to split the bill? \n:"))

total_bill = bill + (bill * (tip_percentage / 100))
bill_pp = round((total_bill / member), 2)
print(f"Each person should pay: {bill_pp}")
