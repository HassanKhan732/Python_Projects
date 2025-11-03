import random

# Word list
words = ["apple", "banana", "mango", "peach"]  # Fixed typo: "mangoo" to "mango"

# Select a random word
length = len(words)
random_word_index = random.randint(0, length - 1)
word = words[random_word_index]
word_length = len(word)

# Initialize game state
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6  # Number of allowed wrong guesses
display_word = ['_'] * word_length  # Start with all underscores

# Randomly reveal 1-3 letters at the start
num_reveal = random.randint(1, min(3, word_length))  # Reveal 1 to 3 letters, capped by word length
revealed_indices = random.sample(range(word_length), num_reveal)
for idx in revealed_indices:
    display_word[idx] = word[idx]
    guessed_letters.append(word[idx])

# Hangman visuals for each stage of wrong guesses
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# Game loop
print("Welcome to Hangman!")
print("The word is:", ' '.join(display_word))
print(hangman_stages[wrong_guesses])

while wrong_guesses < max_wrong_guesses and '_' in display_word:
    # Get player guess
    guess = input("Guess a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    # Check if guess is in the word
    if guess in word:
        print("Good guess!")
        # Update display_word with correct guess
        for i in range(word_length):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")
    
    # Show current game state
    print("\nWord:", ' '.join(display_word))
    print("Guessed letters:", ', '.join(guessed_letters))
    print(hangman_stages[wrong_guesses])

# Game outcome
if '_' not in display_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)