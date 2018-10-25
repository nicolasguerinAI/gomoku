import sys
from Game import Game
from Board import Board

if __name__ == '__main__':
    game = Game()
    game.run()
    game.board.print_board()
    sys.exit(0)
