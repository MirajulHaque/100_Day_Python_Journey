import random

nameAsCSV = input("Give me everybody's names, separated by comma.\n:")
names = nameAsCSV.split(", ")

payer_in = random.randint(0, len(names)-1)
payer = names[payer_in]

print(f"Bill Payer would be: {payer}")
