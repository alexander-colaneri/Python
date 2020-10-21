from random import randint
import P02_database  # Importing data from the "database" file.



# conn.commit()


class SBSystem:
    def __init__(self):
        self.account_initial_numbers = [4, 0, 0, 0, 0, 0]
        self.verified_account_number = []
        self.balance = 0
        self.pin = []
        self.id = 0
        self.main_menu_text = '\n1. Create an account\n2. Log into account\n0. Exit\n'
        self.account_menu_text = '\n1. Balance\n2. Log out\n0. Exit\n'

    # Create account and PIN:
    def create_account_pin(self):
        # Reset numbers, if user wants a different number:
        self.account_initial_numbers = [4, 0, 0, 0, 0, 0]
        self.pin = []
        # Activate the database connection and table creation:
        connection = P02_database.connect()
        P02_database.create_tables(connection)

        # Generate data:
        print('\nYour card has been created\nYour card number:')
        for _ in range(10):
            i = randint(0, 9)
            self.account_initial_numbers.append(i)  # Including random numbers.
        self.luhn_checker()  # Luhn validation.
        number = ''.join(self.verified_account_number)
        print(number)
        print('Your card PIN: ')
        for _ in range(4):
            j = randint(0, 9)
            self.pin.append(str(j))
        pin = ''.join(self.pin)
        print(pin)
        balance = self.balance
        #  Insert data into database:
        P02_database.insert_data_to_database(connection, number, pin, balance)

        # cur.execute('INSERT INTO card (id, number, pin, balance) VALUES (self.id, number, pin, self.balance)')
        # conn.commit()
        # print(cur.fetchall())


    def luhn_checker(self):
        analysis = list(self.account_initial_numbers)
        analysis[-1] = 0  # Annulment of the last number, replacing with "0".
        for i in range(len(analysis)):
            if i % 2 == 0:
                analysis[i] *= 2
                if analysis[i] >= 9:
                    analysis[i] -= 9
        if sum(analysis) % 10 > 0:
            checksum = 10 - (sum(analysis) % 10)
        else:
            checksum = 0  # When the remainder of % 10 is "0", the checksum
            # is "0". Otherwise, we would have a card with 17 digits.
        self.account_initial_numbers[-1] = checksum
        self.verified_account_number = [str(s) for s in self.account_initial_numbers]

    # Menus:
    def main_menu(self):
        while (option := input(self.main_menu_text)) != "0":
            if option == "1":
                self.create_account_pin()
            elif option == "2":
                self.log_in()
            else:
                print('\nInvalid option')
        print('\nBye!')


    def account_menu(self):
        while True:
            option = input(self.account_menu_text)
            if option == "1":
                print(self.balance)
            elif option == "2":
                print('\nYou have successfully logged out!')
                break
            elif option == 0:
                print('\nBye!')
                exit()
            else:
                print('\nInvalid option')


    # Log in and PIN:
    def log_in(self):
        print('\nEnter your card number:')
        card_number_input = input()
        print('Enter your PIN')
        pin_input = input()

        if len(card_number_input) != 16 or len(pin_input) != 4:
            print('\nWrong card number or PIN!')
        else:
            if card_number_input == ''.join(self.verified_account_number) and \
                    pin_input == ''.join(self.pin):
                print('\nYou have successfully logged in!')
                self.account_menu()
            else:
                print('\nWrong card number or PIN!')


sbsystem = SBSystem()
sbsystem.main_menu()
