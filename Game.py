import AI
import Board
import CommandParser
from Board import Board
from AI import AI

# About Constants
NAME = "pbrain"
VERSION = "1.0"
AUTHOR = "Nicolas GUERIN & Jeremiah DECOMBE"
COUNTRY = "France"

# IDs Constant
AI_ID = 1
PLAYER_ID = 2


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI(AI_ID, self.board)
        self.is_active = False

    def __about(self):
        print(f'name=\"{NAME}\", version=\"{VERSION}\", author=\"{AUTHOR}\", country=\"{COUNTRY}\"')

    def loop(self):
        # self.is_active = True
        while self.is_active:
            command, parameters = CommandParser.read_command()
            self.ai.do_command(command, parameters)
