import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

blank_word = []
for n in range(0, len(chosen_word)):
    blank_word += "_"
print(blank_word)
guess = input("Guess a letter: ").lower()

count = 0
for letter in chosen_word:
    if guess == letter:
        blank_word[count] = guess
    elif guess != letter:
        print("Wrong")
    count += 1

print(blank_word)
