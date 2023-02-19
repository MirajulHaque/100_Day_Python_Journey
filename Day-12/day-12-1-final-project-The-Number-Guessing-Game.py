import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game !\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")

game_step_limit = 5
if level == "easy":
    game_step_limit = 10
print(f"You have {game_step_limit} attempts remaining to guess the number.")


random_number = random.randint(1, 100)

while 0 < game_step_limit:
    game_step_limit -= 1
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high")
        print(f"You have {game_step_limit} attempts remaining to guess the number.")
    elif guess < random_number:
        print("Too low.")
        print(f"You have {game_step_limit} attempts remaining to guess the number.")
    elif guess == random_number:
        print("Correct. \nYou win!")
        break
    if game_step_limit == 0:
        print("You lose!")


