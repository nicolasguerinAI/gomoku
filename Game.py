import AI
import Board
from Board import Board
from AI import AI

name = "pbrain"
version = "1.0"
author = "Nicolas GUERIN & Jeremiah DECOMBE"
country = "France"

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI(1, self.board)

    def about(self):
        print(f'name=\"{name}\", version=\"{version}\", author=\"{author}\", country=\"{country}\"')
