import sys
from enum import Enum
from abc import ABC


class ProtocolCommand(Enum):
    ABOUT = 'ABOUT'
    BEGIN = 'BEGIN'
    BOARD = 'BOARD'
    DEBUG = 'DEBUG'
    END = 'END'
    ERROR = 'ERROR message'
    INFO = 'INFO'
    MESSAGE = 'MESSAGE'
    OK = 'OK'
    PLAY = 'PLAY'
    RECTSTART = 'RECTSTART'
    RESTART = 'RESTART'
    START = 'START'
    SUGGEST = 'SUGGEST'
    TAKEBACK = 'TAKEBACK'
    TURN = 'TURN'
    UNKNOWN = 'UNKNOWN'



class Communication(ABC):
    def __init__(self):
        pass

    @staticmethod
    def read_command():
        line = sys.stdin.readline()
        words = line.split()


    @staticmethod
    def send_command(command, msg):
        print(command.value + " " + msg)
