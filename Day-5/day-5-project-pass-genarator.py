import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']

print("Welcome to the Python Password Generator")
nf_letters = int(input("How many letters would you like in your password?\n:"))
nf_numbers = int(input("How many numbers would you like in your password?\n:"))
nf_symbols = int(input("How many symbols would you like in your password?\n:"))

# Easy Generator

# password = ""
# for char in range(1, nf_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nf_numbers + 1):
#     password += random.choice(numbers)
#
# for char in range(1, nf_symbols + 1):
#     password += random.choice(symbols)
#
# # print(password)

# Advanced Generator
password_list = []
for char in range(1, nf_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nf_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, nf_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)

