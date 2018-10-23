import sys

import AI
import Board
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

    # Game Command Executions
    def cmd_ABOUT(self, parameters):
        print(f'name=\"{NAME}\", version=\"{VERSION}\", author=\"{AUTHOR}\", country=\"{COUNTRY}\"')

    def cmd_UNKNOWN(self, parameters):
        print(f'UNKNOWN Unknown command : {parameters}')

    def cmd_END(self, parameters):
        sys.exit(0)

    # Game Command Switcher
    def __do_game_command(self, command, parameters):
        attr_name = "cmd_" + command.value
        try:
            self.__getattribute__(attr_name)(parameters)
            return True
        except Exception:
            return False

    # Main Loop
    def loop(self):
        while 1:
            command, parameters = Communication.read_command()
            if not self.__do_game_command(command, parameters):
                self.ai.do_command(command, parameters)
