import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_photos = [rock, paper, scissors]

user_input = int(input("Enter your choice, \n0 for Rock \n1 for Paper\n2 for Scissor\n:"))
if user_input < 0 or user_input > 2:
    print("You entered a wrong number! You lose.")
else:
    user_choice = game_photos[user_input]
    print(f"\nYou Chose:\n{user_choice}")

    computer_input = random.randint(0, 2)
    computer_choice = game_photos[computer_input]
    print(f"Computer Chose:\n{computer_choice}")

    if user_input == 0 and computer_input == 2:
        print("You win.")
    elif user_input == 2 and computer_input == 0:
        print("You lose.")
    elif user_input > computer_input:
        print("You win")
    elif user_input < computer_input:
        print("You lose.")
    elif user_input == computer_input:
        print("Game Draw.")
print("Game Over")
