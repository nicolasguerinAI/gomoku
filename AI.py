import random
import Game

class AI(object):

    def __init__(self, id, board):
        self.id = id
        self.board = board

    def __get_max(self, bound_min, bound_max, id):
        max_x = 0
        max_y = 0
        max_score = 0
        tmp = 0

        for x in range(bound_min[0], bound_max[0]):
            for y in range(bound_min[1], bound_max[1]):
                if self.board.check_token(x, y) == False:
                    continue
                tmp = self.board.count_token(x, y, id)
                if tmp > max_score:
                    max_score = tmp
                    max_x = x
                    max_y = y

        return max_x, max_y, max_score

    def __play(self):
        bound_min = [0, 0]
        bound_max = [self.board.size, self.board.size]
        x_ai, y_ai, score_ai = self.__get_max(bound_min, bound_max, Game.AI_ID)
        x_player, y_player, score_player = self.__get_max(bound_min, bound_max, Game.PLAYER_ID)

        if score_ai == 0 and score_player == 0:
            x, y = random.randint(0, 18), random.randint(0, 18)
            print(f'{x},{y}')
        elif score_player > score_ai:
            self.board.add_token(Game.AI_ID, x_player, y_player)
            print(f'{x_player},{y_player}')
        else:
            self.board.add_token(Game.AI_ID, x_ai, y_ai)
            print(f'{x_ai},{y_ai}')

    def cmd_TURN(self, parameters):
        param_list = parameters[0].split(",")
        self.board.add_token(Game.PLAYER_ID, int(param_list[0]), int(param_list[1]))
        self.__play()

    def cmd_BEGIN(self, parameters):
        self.__play()

    def do_command(self, command, parameters):
        attr_name = "cmd_" + command.value
        try:
            self.__getattribute__(attr_name)(parameters)
        except Exception as e:
            print(f'Command \"{command.value}\" not yet implemented.')

