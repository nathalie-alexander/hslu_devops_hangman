import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word_to_guess = input("Enter a word for others to guess: ").strip().upper()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_attempts = 8
        self.correct_guesses = set()

    
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
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
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

    def display_word(self):
        display = [letter if letter in self.correct_guesses else '_' for letter in self.word_to_guess]
        return ' '.join(display)

    def display_hangman(self):
        print(self.HANGMAN_PICS[self.wrong_guesses])

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'. Try again.")
        elif letter in self.word_to_guess:
            print(f"Good guess! '{letter}' is in the word.")
            self.correct_guesses.add(letter)
        else:
            print(f"Sorry, '{letter}' is not in the word.")
            self.wrong_guesses += 1
        self.guessed_letters.add(letter)

    def game_status(self):
        if self.wrong_guesses >= self.max_attempts:
            return "lost"
        elif all(letter in self.correct_guesses for letter in self.word_to_guess):
            return "won"
        return "ongoing"

    def play(self):
        print("Welcome to Hangman!")
        print("Try to guess the word, one letter at a time.")

        while self.game_status() == "ongoing":
            print("\n" + self.display_word())
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
            print(f"Remaining attempts: {self.max_attempts - self.wrong_guesses}")
            guess = input("Guess a letter: ").strip()

            if len(guess) == 1 and guess.isalpha():
                self.guess_letter(guess)
            else:
                print("Please enter a single letter.")

        if self.game_status() == "won":
            print(f"\nCongratulations! You've won! The word was '{self.word_to_guess}'.")
        else:
            print(f"\nGame over! You've run out of attempts. The word was '{self.word_to_guess}'.")

# Word list for the game
words = ["python", "hangman", "programming", "development", "console"]

# Start the game
game = Hangman(words)
game.play()
