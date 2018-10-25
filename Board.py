import sys


class Board(object):
    def __init__(self):
        self.size = 19
        self.current_id = 0
        self.board = self.__create_board()

    # private
    def __create_board(self):
        board = [[0] * self.size for i in range(0, self.size)]
        return board

    def __check_horizontal(self, x, y):
        start_x = max(x - 5, 0)
        end_x = min(x + 5, self.size - 1)
        return self.__check_line(start_x, y, end_x, y, x, y)

    def __check_vertically(self, x, y):
        start_y = max(y - 5, 0)
        end_y = min(y + 5, self.size - 1)
        return self.__check_line(x, start_y, x, end_y, x, y)

    def __check_slash(self, x, y):
        start_x = max(x - 5, 0)
        start_y = max(y - 5, 0)
        end_x = min(x + 5, self.size - 1)
        end_y = min(y + 5, self.size - 1)
        return self.__check_line(start_x, start_y, end_x, end_y, x, y)

    def __check_antislash(self, x, y):
        start_x = max(x - 5, 0)
        start_y = min(y + 5, self.size - 1)
        end_x = min(x + 5, self.size - 1)
        end_y = max(y - 5, 0)
        return self.__check_line(start_x, start_y, end_x, end_y, x, y)

    def __check_line(self, start_x, start_y, end_x, end_y, x, y):
        cur_length = 0

        for curX in range(start_x, end_x + 1):
            for curY in range(start_y, end_y + 1):
                if self.board[curY][curX] == self.current_id or (curX == x and curY == y):
                    cur_length = cur_length + 1
                else:
                    cur_length = 0
                if cur_length == 5:
                    return True

        return False

    # public
    def add_token(self, id, pos_x, pos_y):
        if self.board[pos_y][pos_x] == 0:
            self.board[pos_y][pos_x] = id
        else:
            return 84

    def check_win(self, x, y, player_id):
        self.current_id = player_id
        if self.__check_horizontal(x, y) or \
                self.__check_vertically(x, y) or \
                self.__check_slash(x, y) or \
                self.__check_antislash(x, y):
            return True
        return False

    def check_token(self, x, y):
        if self.board[x][y] == 0:
            return True
        else:
            return False

    if __debug__:
        def print_board(self):
            for lines in self.board:
                for token in lines:
                    sys.stdout.write(str(token))
                print()
