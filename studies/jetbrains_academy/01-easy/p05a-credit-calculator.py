from math import ceil, log


class CreditCalculator:
    def __init__(self):
        self.principal = 0
        self.months = 0
        self.monthly_payment = 0
        self.last_payment = 0
        self.interest = 0
        self.menu_text = 'What do you want to calculate?\n' \
                         'type "n" for the number of months,\n' \
                         'type "a" for the annuity monthly payment,\n' \
                         'type "p" for the credit principal, \n' \
                         'type "d" for differentiated payments: '
        self.option = ''

    # Inputs:
    def ask_principal(self):
        print('Enter credit principal: ')
        self.principal = int(input())

    def ask_monthly_payment(self):
        print('Enter the monthly payment: ')
        self.monthly_payment = float(input())

    def ask_months(self):
        print('Enter the number of periods: ')
        self.months = int(input())

    def ask_interest(self):
        print('Enter the credit interest: ')
        percentage = float(input())
        self.interest = percentage / 100 / 12

    # Start:
    def main_menu(self):
        print(self.menu_text)
        self.option = input().lower().strip()
        if self.option == 'n':
            self.calc_months_n()
        elif self.option == 'a':
            self.calc_monthly_payment_a()
        elif self.option == 'p':
            self.calc_principal_p()
        elif self.option == 'd':
            self.calc_diff_payment()
        else:
            print('Invalid option')

    # Calculation:
    def calc_months_n(self):
        self.ask_principal()
        self.ask_monthly_payment()
        self.ask_interest()
        self.months = ceil(log(self.monthly_payment / (self.monthly_payment - self.interest * self.principal), 1 + self.interest))
        if self.months < 12:
            print(f'\nIt takes {self.months:.0f} {"month" if self.months == 1 else "months"} to repay this credit!')
        else:
            years = self.months // 12  # full complete years.
            months_with_years = self.months % 12  # the remainder = months.
            if years >= 1 and months_with_years == 0:
                print(f'You need {years} {"year" if years == 1 else "years"} to repay this credit!')
            else:
                print(f'You need {years} {"year" if years == 1 else "years"} and '
                      f'{months_with_years} {"month" if months_with_years == 1 else "months"} to repay this credit!')
            print(f'Overpayment = {int((self.monthly_payment * self.months) - self.principal)}')

    def calc_monthly_payment_a(self):
        self.ask_principal()
        self.ask_months()
        self.ask_interest()
        divider = pow(1 + self.interest, self.months) - 1
        self.monthly_payment = ceil(self.principal * self.interest * pow((1 + self.interest), self.months) / divider)
        print(f'\nYour monthly payment = {self.monthly_payment}!')
        print(f'Overpayment = {self.monthly_payment * self.months - self.principal}')

    def calc_principal_p(self):
        self.ask_monthly_payment()
        self.ask_months()
        self.ask_interest()
        self.principal = round(self.monthly_payment /
                               ((self.interest * pow(1 + self.interest, self.months)) / (pow(1 + self.interest, self.months) - 1)))
        print(f'Your credit principal = {self.principal}!')
        print(f'Overpayment = {int(self.monthly_payment * self.months - self.principal)}')

    def annuity_payment(self):
        self.ask_monthly_payment()
        self.ask_months()
        self.ask_interest()

    def calc_diff_payment(self):
        overpayment = 0
        self.ask_principal()
        self.ask_months()
        self.ask_interest()
        if not self.principal or not self.months or not self.interest:
            print('Invalid parameters')
        elif self.principal < 0 or self.months < 0 or self.interest < 0:
            print('Invalid parameters')
        else:
            for m in range(1, self.months + 1):
                diff = ceil(self.principal / self.months + self.interest * (self.principal - (self.principal * (m - 1) / self.months)))
                overpayment += diff
                print(f'Month {m}: payment is {diff}')
            print()
            print(f'Overpayment = {overpayment - self.principal}')


creditcalculator = CreditCalculator()
creditcalculator.main_menu()
