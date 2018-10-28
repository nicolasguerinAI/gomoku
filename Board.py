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

    def __count_horizontal(self, x, y):
        start_x = max(x - 5, 0)
        end_x = min(x + 5, self.size - 1)
        return self.__count_line(start_x, y, end_x, y)

    def __count_vertically(self, x, y):
        start_y = max(y - 5, 0)
        end_y = min(y + 5, self.size - 1)
        return self.__count_line(x, start_y, x, end_y)

    def __count_antislash(self, x, y):
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0

        start_dist_x = abs(x - max(x - 5, 0))
        start_dist_y = abs(y - max(y - 5, 0))
        start_x = x - min(start_dist_x, start_dist_y)
        start_y = y - min(start_dist_x, start_dist_y)

        end_dist_x = abs(x - min(x + 5, self.size - 1))
        end_dist_y = abs(y - min(y + 5, self.size - 1))
        end_x = x + min(end_dist_x, end_dist_y)
        end_y = y + min(end_dist_x, end_dist_y)

        return self.__count_line(start_x, start_y, end_x, end_y)

    def __count_slash(self, x, y):
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0

        start_dist_x = abs(x - max(x - 5, 0))
        start_dist_y = abs(y - min(y + 5, self.size - 1))
        start_x = x - min(start_dist_x, start_dist_y)
        start_y = y + min(start_dist_x, start_dist_y)

        end_dist_x = abs(x - min(x + 5, self.size - 1))
        end_dist_y = abs(y - max(y - 5, 0))
        end_x = x + min(end_dist_x, end_dist_y)
        end_y = y - min(end_dist_x, end_dist_y)

        return self.__count_line(start_x, start_y, end_x, end_y)

    def __count_line(self, start_x, start_y, end_x, end_y):
        cur_length = 0
        cur_max = 0
        x_idx = 0 if end_x - start_x == 0 else int((end_x - start_x)/(abs(end_x - start_x)))
        y_idx = 0 if end_y - start_y == 0 else int((end_y - start_y)/(abs(end_y - start_y)))

        while start_x != end_x or start_y != end_y:
            if self.board[start_y][start_x] == self.current_id:
                cur_length = cur_length + 1
            else:
                cur_max = max(cur_max, cur_length)
                cur_length = 0
            start_x = start_x + x_idx
            start_y = start_y + y_idx

        return cur_max

    # public
    def add_token(self, id, pos_x, pos_y):
        if self.board[pos_y][pos_x] == 0:
            self.board[pos_y][pos_x] = id
        else:
            return 84

    def count_token(self, x, y, player_id):
        self.current_id = player_id
        h_max = self.__count_horizontal(x, y)
        v_max = self.__count_vertically(x, y)
        s_max = self.__count_slash(x, y)
        a_max = self.__count_antislash(x, y)
        return max(h_max, v_max, s_max, a_max)

    def check_token(self, x, y):
        if self.board[y][x] == 0:
            return True
        else:
            return False

    if __debug__:
        def print_board(self):
            for lines in self.board:
                for token in lines:
                    sys.stdout.write(str(token))
                print()
