from random import choice


class Hangman:
    # Game immutable variables (class attributes):
    words = ['python', 'java', 'kotlin', 'javascript']
    game_name = 'H A N G M A N'
    menu_message = 'Type "play" to play the game, "exit" to quit: '
    ask_letter_message = 'Input a letter: '
    win_message = 'You guessed the word!\nYou survived!\n'
    lose_message = 'You are hanged!\n'
    no_letter_message = 'No such letter in the word'
    repeated_letter_message = 'You already typed this letter'
    not_ASCII_message = 'It is not an ASCII lowercase letter'
    not_single_message = 'You should input a single letter'

    # Game mutable variables (instance attributes):
    def __init__(self):
        self.lives = 8
        self.counter_times_played = 0  # Used to display name of the game once.
        # Attributes that will be written during the game, but already listed:
        self.hidden_word = []
        self.pc_choice = ''
        self.word_set = ''
        self.user_letter = ''
        self.main_menu_option = ''
        self.already_typed = set()  # Remember: sets run faster than lists.

    def main_menu(self):
        # Display name of the game just once.
        if self.counter_times_played == 0:
            print(Hangman.game_name)
            self.counter_times_played += 1

        while True:
            self.main_menu_option = input(Hangman.menu_message)
            if self.main_menu_option == 'play':
                # When the player chooses to play, variables are composed.
                self.pc_choice = list(choice(Hangman.words))
                self.hidden_word = list('-' * len(self.pc_choice))
                # Set created -> more speed in letter verification (line 94):
                self.word_set = set(self.pc_choice)
                self.start_game()

            elif self.main_menu_option == 'exit':
                break

    # Game inputs and win/lose states:
    def start_game(self):
        while True:
            print()  # This detail was necessary to accomplish the exercise.
            self.check_hidden_word()
            self.user_letter = input(Hangman.ask_letter_message)
            self.game_mechanics()

            if self.hidden_word == self.pc_choice:
                self.check_hidden_word()
                print(Hangman.win_message)
                self.already_typed = set()  # Reset set of repeated characters.
                self.lives = 8  # Reset lives.
                break

            if self.lives == 0:
                print(Hangman.lose_message)
                self.already_typed = set()  # Reset set of repeated characters.
                self.lives = 8  # Reset lives.
                break

    # Game checking area:
    def check_lives(self):
        if self.lives > 0:
            self.lives -= 1

    def check_hidden_word(self):
        print(''.join(self.hidden_word))

    # Game data processing (attention to "if"/"elif" sequence):
    def game_mechanics(self):
        for c in range(len(self.pc_choice)):
            if len(self.user_letter) >= 2:
                print(Hangman.not_single_message)
                return

            elif not self.user_letter.islower() or \
                    self.user_letter == '-':
                print(Hangman.not_ASCII_message)
                return

            elif self.user_letter == self.hidden_word[c] or \
                    self.user_letter in self.already_typed:
                print(Hangman.repeated_letter_message)
                return

            elif self.user_letter not in self.word_set:
                self.check_lives()
                self.already_typed.add(self.user_letter)
                print(Hangman.no_letter_message)
                return

            elif self.user_letter == self.pc_choice[c]:
                self.hidden_word[c] = self.user_letter


hangman = Hangman()
hangman.main_menu()
