import random
import Game
class AI:
    def __init__(self, id, board):
        self.id = id
        self.board = board


    def cmd_TURN(self, parameters):
        param_list = parameters[0].split(",")
        self.board.add_token(Game.PLAYER_ID, int(param_list[0]), int(param_list[1]))
        x, y = random.randint(0, 18), random.randint(0, 18)
        while self.board.check_token(x, y) is False:
            x,y = random.randint(0, 18), random.randint(0, 18)
        self.board.add_token(Game.AI_ID, x, y)
        print(f'{x},{y}')

    def cmd_BEGIN(self, parameters):
        x, y = random.randint(0, 18), random.randint(0, 18)
        if self.board.check_token(x, y) is True:
            self.board.add_token(Game.AI_ID, x, y)
            print(f'{x},{y}')
        else:
            self.cmd_TURN(parameters)

    def do_command(self, command, parameters):
        attr_name = "cmd_" + command.value
        try:
            self.__getattribute__(attr_name)(parameters)
        except Exception as e:
            print(f'Command \"{command.value}\" not yet implemented.')

