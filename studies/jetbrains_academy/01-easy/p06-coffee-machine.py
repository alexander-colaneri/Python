class CoffeeMachine:
    # Started with class attributes; the ones that won't change.
    resources_names = ['water', 'milk', 'coffee beans', 'disposable cups',
                       'money']
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    def __init__(self):
        # Just in case, I put everything I thought I would use detailed.
        self.action = None
        self.machine = [400, 540, 120, 9, 550]  # Machine initial state.
        self.resources_names = CoffeeMachine.resources_names
        self.espresso = CoffeeMachine.espresso
        self.latte = CoffeeMachine.latte
        self.cappuccino = CoffeeMachine.cappuccino

    def main_menu(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            self.action = input()

            if self.action == 'buy':
                CoffeeMachine.select_beverage(self)
            elif self.action == 'fill':
                CoffeeMachine.fill(self)
            elif self.action == 'take':
                CoffeeMachine.take(
                    self)  # "Self here, self there, self everywhere"!
            elif self.action == "remaining":
                CoffeeMachine.display_state(self)
            elif self.action == 'exit':
                break
            else:
                print('Invalid action!')

    def select_beverage(self):
        print('What do you want to buy? 1 - espresso , 2 - latte, '
              '3 - cappuccino, back - to main menu')
        option = input()
        if option == '1':
            return self.calculate_supplies(self.espresso)  # I had no idea,
            # until then, that I had to put "self." BEFORE the method too!
            # PyCharm gave me this suggestion.
        elif option == '2':
            return self.calculate_supplies(self.latte)
        elif option == '3':
            return self.calculate_supplies(self.cappuccino)
        elif option == 'back':
            return

    def calculate_supplies(self, type_coffee):  # Almost forgot to put the
        # parameter here (type_coffee) that would receive the return (list
        # of ingredients and cost) from my "select_beverage" method.

        for c in range(4):
            if self.machine[c] <= type_coffee[c]:  # Some iteration to
                # compare supplies in machine with ingredients lists.
                print(f'Sorry, not enough {self.resources_names[c]}!')
                return
        print('I have enough resources, making you a coffee!')

        for b in range(5):
            if b < 4:
                self.machine[b] -= type_coffee[b]  # Here we're dealing with
                # ingredients (indexes 0 to 3)...
            else:
                self.machine[4] += type_coffee[4]  # ... and here, with cash.

    def fill(self):

        print('Write how many ml of water do you want to add:')
        qt_water = int(input())
        self.machine[0] += qt_water

        print('Write how many ml of milk do you want to add:')
        qt_milk = int(input())
        self.machine[1] += qt_milk

        print('Write how many grams of coffee beans do you want to add:')
        qt_coffee = int(input())
        self.machine[2] += qt_coffee

        print('Write how many disposable cups of coffee do you want to add:')
        qt_disposable_cups = int(input())
        self.machine[3] += qt_disposable_cups

    # self, self, self...

    def take(self):

        print(f'I gave you ${self.machine[4]}')
        self.machine[4] -= self.machine[4]

    def display_state(self):
        print('The coffee machine has:')
        for c in range(4):
            print(f'{self.machine[c]} of {self.resources_names[c]}')
        print(f'${self.machine[4]} of {self.resources_names[4]}')


start = CoffeeMachine()
start.main_menu()

# Have a nice day!
