import sys

from Communication import Communication
from Board import Board
from AI import AI

# About Constants
NAME = "pbrain"
VERSION = "1.0"
AUTHOR = "Nicolas GUERIN & Jeremiah DECOMBE"
COUNTRY = "Nouvelle-Calédonie"

# IDs Constant
AI_ID = 1
PLAYER_ID = 2

class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI(AI_ID, self.board)
        self.timeout_turn = 0
        self.timeout_match = 0
        self.max_memory = 0
        self.time_left = 0
        self.game_type = 0
        self.rule = 1
        self.evaluate = ""
        self.folder = ""
        self.end = False

    # Game Command Executions
    def cmd_ABOUT(self, parameters):
        print(f'name=\"{NAME}\", version=\"{VERSION}\", author=\"{AUTHOR}\", country=\"{COUNTRY}\"')

    def cmd_UNKNOWN(self, parameters):
        print(f'UNKNOWN Unknown command : {parameters}')

    def cmd_END(self, parameters):
        self.end = True

    def cmd_START(self, parameters):
        print("OK")

    def cmd_BOARD(self, parameters):
        for parameter in parameters:
            parameter_as_list = parameter.split(",")
            if len(parameter_as_list) != 3:
                print("ERROR")
                return
            self.board.add_token(int(parameter_as_list[2]), int(parameter_as_list[0]), int(parameter_as_list[1]))

    def cmd_INFO(self, parameters):
        if self.__dict__.__contains__(parameters[0]) and len(parameters) is 2:
            self.__dict__[parameters[0]] = parameters[1]
        else:
            print("ERROR")

    # Game Command Switcher
    def __do_game_command(self, command, parameters):
        attr_name = "cmd_" + command.value
        try:
            self.__getattribute__(attr_name)(parameters)
            return True
        except Exception:
            return False

    # Main Loop
    def run(self):
        while not self.end:
            command, parameters = Communication.read_command()
            if not self.__do_game_command(command, parameters):
                self.ai.do_command(command, parameters)
            sys.stdout.flush()
