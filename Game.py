import AI
import Board

name = "pbrain"
version = "1.0"
author = "Nicolas GUERIN & Jeremiah DECOMBE"
country = "France"

class Game:
    def __init__(self):
        self.board = self.board.Board()
        self.ai = self.ai.AI()

    def about(self):
        print(f'name=\"{name}\", version=\"{version}\", author=\"{author}\", country=\"{country}\"')
