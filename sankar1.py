import random

def hangman():
    # List of predefined words
    words = ["python", "program", "developer", "hangman", "computer"]
    
    # Randomly choose one word
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    word_display = ["_"] * len(word)

    print("Welcome to Hangman Game!")
    print("You have", attempts, "incorrect guesses allowed.")
    print(" ".join(word_display))
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)

        print(" ".join(word_display))

        # Check if player has guessed all letters
        if "_" not in word_display:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

    if "_" in word_display:
        print("\n😞 Out of attempts! The word was:", word)

# Run the game
if __name__=="__main__":
    hangman()