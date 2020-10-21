from random import randint
import sqlite3


class SBSystem:
    def __init__(self):
        self.account_initial_numbers = [4, 0, 0, 0, 0, 0]
        self.verified_account_number = []
        self.pin = []
        self.active_account = ''
        self.main_menu_text = '\n1. Create an account\n2. Log into account\n0. Exit\n'
        self.account_menu_text = '\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n'

    # SQL - CREATE:
    @staticmethod  # Static method: when we´re not using any attributes from
    # the constructor above.
    def create_tables():
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        CREATE_CARD_TABLE = 'CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY ' \
                            'KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);'
        return cur.execute(CREATE_CARD_TABLE)

    # SQL - INSERT/UPDATE
    @staticmethod
    def insert_data_to_database(number, pin, balance):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        INSERT_ACCOUNT_DATA = "INSERT INTO card (number, pin, balance) VALUES (?, ?, ?)"
        cur.execute(INSERT_ACCOUNT_DATA, (number, pin, balance))
        return conn.commit()

    @staticmethod
    def money_transference_add(income, account_number):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        MONEY_TRANSFERENCE_ADD = "UPDATE card SET balance = balance + (?) WHERE number = (?)"
        cur.execute(MONEY_TRANSFERENCE_ADD, (income, account_number))
        return conn.commit()

    @staticmethod
    def money_transference_sub(income, account_number):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        MONEY_TRANSFERENCE_ADD = "UPDATE card SET balance = balance - (?) WHERE number = (?)"
        cur.execute(MONEY_TRANSFERENCE_ADD, (income, account_number))
        return conn.commit()

    # SQL - SELECT:
    @staticmethod
    def search_number_in_database(number):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        SEARCH_NUMBER = 'SELECT number FROM card WHERE number = (?);'
        return cur.execute(SEARCH_NUMBER, (number,)).fetchone()

    @staticmethod
    def balance_mod(active_account):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        BALANCE = 'SELECT balance FROM card WHERE number = (?);'
        return cur.execute(BALANCE, (active_account,)).fetchone()

    @staticmethod
    def login_verifier(number, pin):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        LOGIN = 'SELECT number, pin FROM card WHERE number = (?) AND pin = (?);'
        return cur.execute(LOGIN, (number, pin)).fetchone()

    # SQL - DELETE:
    @staticmethod
    def close_account(account_number):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        CLOSE_ACCOUNT = 'DELETE FROM card WHERE number = (?);'
        cur.execute(CLOSE_ACCOUNT, (account_number,))
        conn.commit()

    # Menus:
    def main_menu(self):
        self.create_tables()  # We need to confirm that we have a database
        # and table created, at the beginning of all.
        while (option := input(self.main_menu_text)) != "0":
            if option == '1':
                self.create_account_pin()
            elif option == '2':
                self.log_in()
            else:
                print('\nInvalid option')
        print('\nBye!')

    def account_menu(self):
        while True:
            option = input(self.account_menu_text)
            if option == '1':
                print(self.balance_mod(self.active_account))
            elif option == '2':
                print('Enter income:')
                income = int(input())
                self.money_transference_add(income, self.active_account)
                print('Income was added!')
            elif option == '3':
                self.transfer()
            elif option == '4':
                self.close_account(self.active_account)
            elif option == '5':
                print('\nYou have successfully logged out!')
                break
            elif option == '0':
                print('\nBye!')
                exit()
            else:
                print('\nInvalid option')

    # Create Account and PIN:
    def create_account_pin(self):
        # Reset numbers, if user wants a different number:
        self.account_initial_numbers = [4, 0, 0, 0, 0, 0]
        self.pin = []
        # Generate data:
        for _ in range(10):
            i = randint(0, 9)
            self.account_initial_numbers.append(i)  # Including random numbers.
        self.luhn_number_generator(
            self.account_initial_numbers)  # Luhn validation.
        number = ''.join(self.verified_account_number)
        print('\nYour card has been created\nYour card number:')
        print(number)
        for _ in range(4):
            j = randint(0, 9)
            self.pin.append(str(j))
        pin = ''.join(self.pin)
        print('Your card PIN: ')
        print(pin)
        balance = 0
        #  Insert data into database:
        return self.insert_data_to_database(number, pin, balance)

    # Luhn:
    def luhn_number_generator(self, number):
        analysis = list(number)
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
        self.verified_account_number = [str(s) for s in
                                        self.account_initial_numbers]
        return self.verified_account_number

    @staticmethod
    def luhn_number_verifier(number):
        num_str = list(number)
        num = [int(i) for i in number]
        num[-1] = 0  # Annulment of the last number, replacing with "0".
        for i in range(len(num)):
            if i % 2 == 0:
                num[i] *= 2
                if num[i] >= 9:
                    num[i] -= 9
        if sum(num) % 10 > 0:
            checksum = str(10 - (sum(num) % 10))
        else:
            checksum = "0"
        num_str[-1] = checksum
        return ''.join(num_str) == number

    def transfer(self):
        while True:
            print('Enter card number:')
            account_to_receive = input()
            # print(f'Luhn Verificador: {self.luhn_number_verifier(account_to_receive)}')
            # print(f'Conta Ativa: {self.active_account}')
            # print(f'Conta a Receber: {account_to_receive}')
            # print(f'Balance: {self.balance_mod(self.active_account)}')
            if self.luhn_number_verifier(account_to_receive):
                if account_to_receive != self.active_account:
                    if self.search_number_in_database(account_to_receive):
                        print('Enter how much money you want to transfer:')
                        value = int(input())
                        if (value, ) > self.balance_mod(self.active_account):
                            print('Not enough money!')
                            break
                        else:
                            self.money_transference_add(value, account_to_receive)
                            self.money_transference_sub(value, self.active_account)
                            break
                    else:
                        print('Such a card does not exist.')
                        break
                else:
                    print("You can't transfer money to the same account!")
                    break
            else:
                print(
                    'Probably you made a mistake in the card number. '
                    'Please try again!')
                break

    # Log in and PIN:
    def log_in(self):
        print('\nEnter your card number:')
        card_number_input = input()
        print('Enter your PIN')
        pin_input = input()
        if len(card_number_input) != 16 or len(pin_input) != 4:
            print('\nWrong card number or PIN!')
        else:
            if self.login_verifier(card_number_input, pin_input):
                print('\nYou have successfully logged in!')
                self.active_account = card_number_input
                self.account_menu()
            else:
                print('\nWrong card number or PIN!')


sbsystem = SBSystem()
sbsystem.main_menu()
