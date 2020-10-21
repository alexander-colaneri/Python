class TicTacToe:
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.matrix = [self.cells[0:3], self.cells[3:6], self.cells[6:9]]
        # Vertical lines list, to be divided in 3 inner lists:
        self.v_lines = []
        # Diagonal lines:
        self.d1_line = [self.matrix[0][0], self.matrix[1][1],
                        self.matrix[2][2]]
        self.d2_line = [self.matrix[0][2], self.matrix[1][1],
                        self.matrix[2][0]]
        self.x_list = ['X', 'X', 'X']
        self.o_list = ['O', 'O', 'O']
        self.turn_counter = 0
        self.end_game = False
        self.coord_input = ''

    def vertical_lines_list(self):  # Transforming vertical sequences in list.
        for c in range(3):
            self.v_lines.append([self.matrix[0][c], self.matrix[1][c],
                                 self.matrix[2][c]])

    def game_start(self):
        self.vertical_lines_list()
        self.display()
        self.game_mechanism()

    def check_input(self, input_):
        forbidden = '4567890'
        if input_.replace(' ', '').isalpha():
            print('You should enter numbers!')
            self.game_mechanism()  # Start over again, if wrong.
        elif len(input_.replace(' ', '')) < 2:  # When only one number digited.
            print('Coordinates must have 2 numbers!')
            self.game_mechanism()
        elif input_[0] in forbidden or input_[2] in forbidden:
            print('Coordinates should be from 1 to 3!')
            self.game_mechanism()
        else:
            # If input is ok, converted to integer.
            self.coord_input = [int(i) for i in input_.replace(' ', '')]
        return self.coord_input

    def game_mechanism(self):
        while not self.end_game:
            user = input('Enter coordinates: ')
            self.check_input(user)

            # Coordinates:
            # (1, 3)(2, 3)(3, 3)
            # (1, 2)(2, 2)(3, 2)
            # (1, 1)(2, 1)(3, 1)

            # This following loop works to convert inputs into indexes,
            # at the same time it helps to validate results:
            for c in range(1, 4):
                if not self.end_game:  # Used to stop some for loops later,
                    # that were showing messages 3 times.
                    if self.coord_input == [c, 3]:  # Line 1.
                        if self.matrix[0][c - 1] == 'X' or \
                                self.matrix[0][c - 1] == 'O':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.turn_counter += 1
                            if self.turn_counter % 2 == 0:  # 'O' is put when
                                # turn_counter is even.
                                self.matrix[0][c - 1] = 'O'  # Hr. ln. check.
                                self.v_lines[c - 1][0] = 'O'  # Vt. ln. check.
                                if c == 1:
                                    self.d1_line[0] = 'O'
                                elif c == 3:
                                    self.d2_line[2] = 'O'
                            else:
                                self.matrix[0][c - 1] = 'X'
                                self.v_lines[c - 1][0] = 'X'
                                if c == 1:
                                    self.d1_line[0] = 'X'
                                elif c == 3:
                                    self.d2_line[2] = 'X'
                            self.display()
                        self.x_win()
                        self.o_win()
                        self.draw()  # Verifying results after each vert. line.

                    elif self.coord_input == [c, 2]:  # Line 2.
                        if self.matrix[1][c - 1] == 'X' or \
                                self.matrix[1][c - 1] == 'O':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.turn_counter += 1
                            if self.turn_counter % 2 == 0:
                                self.matrix[1][c - 1] = 'O'
                                self.v_lines[c - 1][1] = 'O'
                                if c == 2:
                                    self.d1_line[1] = 'O'
                                    self.d2_line[1] = 'O'
                            else:
                                self.matrix[1][c - 1] = 'X'
                                self.v_lines[c - 1][1] = 'X'
                                if c == 2:
                                    self.d1_line[1] = 'X'
                                    self.d2_line[1] = 'X'
                            self.display()
                        self.x_win()
                        self.o_win()
                        self.draw()

                    elif self.coord_input == [c, 1]:  # Line 3.
                        if self.matrix[2][c - 1] == 'X' or \
                                self.matrix[2][c - 1] == 'O':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.turn_counter += 1
                            if self.turn_counter % 2 == 0:
                                self.matrix[2][c - 1] = 'O'
                                self.v_lines[c - 1][2] = 'O'
                                if c == 3:
                                    self.d1_line[2] = 'O'
                                elif c == 1:
                                    self.d2_line[0] = 'O'
                            else:
                                self.matrix[2][c - 1] = 'X'
                                self.v_lines[c - 1][2] = 'X'
                                if c == 3:
                                    self.d1_line[2] = 'X'
                                elif c == 1:
                                    self.d2_line[0] = 'X'
                            self.display()
                        self.x_win()
                        self.o_win()
                        self.draw()

    def display(self):
        print('-' * 9)
        print(f'| {" ".join(self.matrix[0])} |')
        print(f'| {" ".join(self.matrix[1])} |')
        print(f'| {" ".join(self.matrix[2])} |')
        print('-' * 9)

    # Results analysis methods:
    def x_win(self):
        # Diagonal:
        if self.d1_line == self.x_list or self.d2_line == self.x_list:
            print('X wins')
            self.end_game = True
        else:
            for c in range(3):
                if not self.end_game:  # Used to stop for loops
                    # when condition achieved.
                    if self.matrix[c] == self.x_list or \
                            self.v_lines[c] == self.x_list:
                        print('X wins')
                        self.end_game = True

    def o_win(self):
        # Diagonal:
        if self.d1_line == self.o_list or \
                self.d2_line == self.o_list:
            print('O wins')
            self.end_game = True
        else:
            for c in range(3):
                if not self.end_game:  # Used to stop for loops when
                    # condition achieved.
                    if self.matrix[c] == self.o_list or \
                            self.v_lines[c] == self.o_list:
                        print('O wins')
                        self.end_game = True

    def draw(self):
        if not self.end_game:
            if self.turn_counter == 9:
                print('Draw')
                self.end_game = True


tictactoe = TicTacToe()
tictactoe.game_start()
# Have a nice day!
