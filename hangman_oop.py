import os
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1


class Hangman:
    HANGMAN_PICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
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

    def __init__(self):
        self.players = self.initialize_players()
        self.current_player_index = 0
        self.word_list = ["python", "hangman", "developer", "challenge", "programming", "algorithm", "data", "structure"]
        self.reset_game()

    def initialize_players(self):
        players = []
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            name = input(f"Enter the name of player {i + 1}: ")
            players.append(Player(name))
        self.use_random_word = num_players < 2
        return players

    # Switch to the next player
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    # Get the current player
    def current_player(self):
        return self.players[self.current_player_index]

    def reset_game(self):
        # Reset game state
        if self.use_random_word:
            self.word_to_guess = random.choice(self.word_list).upper()
        else:
            self.word_to_guess = input(f"Enter a word for {self.current_player().name} to guess: ").strip().upper()
        self.clear_screen()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_attempts = len(self.HANGMAN_PICS) - 1
        self.correct_guesses = set()

    def clear_screen(self):
        # Clear the screen based on the operating system (when used in terminal)
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For macOS and Linux
            os.system('clear')

    def display_word(self):
        display = [letter if letter in self.correct_guesses else '_' for letter in self.word_to_guess]
        return ' '.join(display)
    
    def display_scores(self):
        print("Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score} points")
        print("\n")

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
    
    def play_again(self):
        # Ask the user if they want to play again
        while True:
            choice = input("Would you like to play again? (y/n): ").strip().lower()
            if choice in ('y', 'n'):
                return choice == 'y'
            print("Invalid input. Please enter 'y' or 'n'.")

    def play(self):
        while True:
            print("Welcome to Hangman!")
            print("Try to guess the word, one letter at a time.")

            while self.game_status() == "ongoing":
                self.display_hangman()
                print("\n" + self.display_word())
                print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
                print(f"Remaining attempts: {self.max_attempts - self.wrong_guesses}")
                guess = input("Guess a letter: ").strip()

                if len(guess) == 1 and guess.isalpha():
                    self.guess_letter(guess)
                else:
                    print("Please enter a single letter.")

            self.display_hangman()

            if self.game_status() == "won":
                self.current_player().add_point()
                print("""
                                    .''.       
        .''.      .        *''*    :_\/_:     . 
        :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
    .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
    :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
    : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
    '..'  ':::'     * /\ *     .'/.\'.   '
        *            *..*         :
        *
            *
                    """)
                print(f"""Congratulations {self.current_player().name}! You've won! The word was '{self.word_to_guess}'.
                      Score: {self.current_player().score} points
                        """)
            else:
                print("""
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    """)
                print(f"\nGame over! The word was '{self.word_to_guess}'.")

            self.display_scores()
            
            if not self.play_again():
                print("Thanks for playing Hangman! Goodbye!")
                break
            self.next_player()
            self.reset_game()

# Start the game
game = Hangman()
game.play()
