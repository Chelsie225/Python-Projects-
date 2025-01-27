import random

hangman_drawings = ['''
  +-----+
  |     |
        |
        |
        |
        |
------------
''', '''
  +-----+
  |     |
  O     |
        |
        |
        |
------------
''', '''
  +-----+
  |     |
  O     |
  |     |
        |
        |
------------
''', '''
  +-----+
  |     |
  O     |
 /|     |
        |
        |
------------
''', '''
  +-----+
  |     |
  O     |
 /|\    |
        |
        |
------------
''', '''
  +-----+
  |     |
  O     |
 /|\    |
 /      |
        |
------------
''', '''
  +-----+
  |     |
  O     |
 /|\    |
 / \    |
        |
------------
''', '''
  +-----+
  |     |
  O     |
 /|\    |
 / \    |
o   o   |
------------
''']

# List of words for different levels
words_by_level = {
    'easy': ['boat', 'walk', 'love', 'tree', 'door'],
    'medium': ['crazy', 'voice', 'quiet', 'month', 'music'],
    'hard': ['humble','vanilla','pencil','device','avatar'],
    'Bonus': ['vertigo','sensible','vivacious','tranquility','gobsmacked']
}

MAX_TRIES = 11
MAX_HINTS = 2  

# Function to choose a random word from the selected level
def get_random_word(level):
    return random.choice(words_by_level[level])

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to check if the player has won
def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function to provide a hint (revealing an unguessed letter)
def provide_hint(word, guessed_letters):
    unguessed_letters = [letter for letter in word if letter not in guessed_letters]
    if unguessed_letters:
        return random.choice(unguessed_letters)
    return None  # In case there are no more unguessed letters

# Function to display the board with hangman drawing
def displayBoard(word, wrong_letters):
    print(hangman_drawings[len(wrong_letters)])
    print(f"Wrong letters: {' '.join(wrong_letters)}")

def playgame():
    print("Welcome to Hangman 2.0. Choose a difficulty level: easy, medium, or hard.")
    while True:
        try:
            level = input("Choose a difficulty level (all lowercase): easy, medium, or hard \n").lower()
            if level not in words_by_level:
                raise ValueError("Invalid level! Please choose 'easy', 'medium', or 'hard'.")
            break
        except ValueError as e:
            print(e)

    word = get_random_word(level)
    guessed_letters = set()
    wrong_letters = []
    tries = MAX_TRIES

    print(f"\nThe word has {len(word)} letters. Let's play!")

    while True:
        displayBoard(word, wrong_letters)
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Tries remaining: {tries - len(wrong_letters)}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print(f"You've already guessed '{guess}'.")
            continue

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            wrong_letters.append(guess)
            print(f"Oops! '{guess}' is not in the word.")

        if check_win(word, guessed_letters):
            print(f"Congratulations! You've guessed the word: {word}")
            break

        if len(wrong_letters) >= tries:
            print(f"You lost! The word was: {word}")
            break

def main():
    while True:
        playgame()
        replay_answer = input("\nDo you want to play again? (yes/no): ")
        if replay_answer.lower() == 'yes':
            continue
        elif replay_answer.lower() == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid answer. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
