class Board:
    def __init__(self, height, width):
        """ constructs a new Board object by initializing the following three attributes:
            height, width, slots
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ returns a string representing a Board object.
        """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'

        for i in range(col + 1):
            s += '--'

        s += '-'

        s += '\n'
        num = 0
        s += ' '
        for i in range(len(self.slots[self.height - 1])):
            if num >= 10:
                num = 0
            s += str(num) + ' '
            num += 1

        return s

    def add_checker(self, checker, col):
        """ that accepts two inputs: checker (either 'X' or 'O'), col, index of
            column
        """
        assert (checker == 'X' or checker == 'O')
        assert (0 <= col < self.width)

        for i in range(1, self.height + 1):
            if self.slots[self.height - i][col] == ' ':
                self.slots[self.height - i][col] = checker
                break

    def reset(self):
        """ reset the Board object on which it is called by setting all slots to contain
            a space character.
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object,
        starting with 'X'.
        """
        checker = 'X'  # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, row, col):
        """ returns True if it is valid to place a checker in the
            column col on the calling Board object. Otherwise, it should return False.
        """

        if self.slots[row][col] == ' ':
            return True
        return False

    def is_full(self):
        """ returns True if the called Board object is completely full of checkers,
            and returns False otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing.
        """
        if self.slots[-1][col] != ' ':
            for i in range(self.height):
                if self.slots[i][col] != ' ':
                    self.slots[i][col] = ' '
                    break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 4):
                if self.slots[row][col] == checker and \
                        self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                        self.slots[row][col + 3] == checker and \
                        self.slots[row][col + 4] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 4):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                        self.slots[row + 3][col] == checker and \
                        self.slots[row + 4][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal downward win for the specified checker.
        """
        for row in range(self.height - 4):
            for col in range(self.width - 4):
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                        self.slots[row + 3][col + 3] == checker and \
                        self.slots[row + 4][col + 4] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal upward win for the specified checker.
        """
        for row in range(1, self.height + 1):
            for col in range(self.width - 4):
                if self.slots[self.height - row][col] == checker and \
                        self.slots[self.height - (row + 1)][col + 1] == checker and \
                        self.slots[self.height - (row + 2)][col + 2] == checker and \
                        self.slots[self.height - (row + 3)][col + 3] == checker and \
                        self.slots[self.height - (row + 4)][col + 4] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ hat accepts a parameter checker that is either 'X' or 'O', and returns True
            if there are four consecutive slots containing checker on the board.
            Otherwise, it should return False.
        """
        assert (checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False



