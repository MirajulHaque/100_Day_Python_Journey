import random
from hangman_word import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)

lives = 6

blank_word = []
for n in range(0, len(chosen_word)):
    blank_word += "_"
print(blank_word)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in blank_word:
        print(f"You've already guessed {guess}")

    count = 0
    for letter in chosen_word:
        if guess == letter:
            blank_word[count] = guess
        count += 1

    print(blank_word)

    if guess not in blank_word:
        print(f"You guessed {guess}, That's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loss.")

    if "_" not in blank_word:
        end_of_game = True
        print("You win")

    print(stages[lives])
