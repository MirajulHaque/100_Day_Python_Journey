import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

blank_word = []
for n in range(0, len(chosen_word)):
    blank_word += "_"
print(blank_word)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    count = 0
    for letter in chosen_word:
        if guess == letter:
            blank_word[count] = guess
        count += 1

    print(blank_word)

    if guess not in blank_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loss.")

    if "_" not in blank_word:
        end_of_game = True
        print("You win")

    print(stages[lives])

