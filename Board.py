import sys


class Board(object):
    def __init__(self):
        self.size = 19
        self.board = self.__create_board()

    # private
    def __create_board(self):
        board = [[0] * self.size for i in range(0, self.size)]
        return board

    def add_token(self, id, pos_x, pos_y):
        if self.board[pos_y][pos_x] == 0:
            self.board[pos_y][pos_x] = id
        else:
            return 84

    if __debug__:
        def print_board(self):
            for lines in self.board:
                for token in lines:
                    sys.stdout.write(str(token))
                print()
