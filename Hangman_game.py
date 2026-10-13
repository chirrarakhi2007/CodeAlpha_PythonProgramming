import random

# List of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Number of incorrect guesses
wrong_guesses = 0

# Maximum allowed incorrect guesses
max_wrong_guesses = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check whether the player has guessed the complete word
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Check if the input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# If the player reaches 6 wrong guesses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)