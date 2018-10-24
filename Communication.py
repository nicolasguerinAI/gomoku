import sys
from enum import Enum
from abc import ABC


class ProtocolCommand(Enum):
    ABOUT = 'ABOUT'
    BEGIN = 'BEGIN'
    BOARD = 'BOARD'
    DEBUG = 'DEBUG'
    END = 'END'
    ERROR = 'ERROR'
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

    @staticmethod
    def get_token(token):
        for pc in ProtocolCommand:
            if pc.value == token:
                return pc
        return ProtocolCommand.UNKNOWN


class Communication(ABC):
    def __init__(self):
        pass

    @staticmethod
    def read_command():
        x = 0
        lines = []
        text = sys.stdin.readline()
        text = text.rstrip()
        if text == 'BOARD':
            lines.append(text)
            while True:
                line = input()
                if line:
                    if line == 'DONE':
                        break
                    lines.append(line)
                else:
                    break
            text = '\n'.join(lines)

        words = text.split()
        token = ProtocolCommand.UNKNOWN
        msgs = []

        if len(words) > 2:
            for word in words:
                if x == 0:
                    x = 1
                    continue
                msgs.append(word)
        elif len(words) > 1:
            msgs.append(words[1])

        if len(words) > 0:
            token = ProtocolCommand.get_token(words[0])
            if token == ProtocolCommand.UNKNOWN:
                msgs = words[0]
        sys.stdin.flush()
        return token, msgs

    @staticmethod
    def send_command(token, msg):
        print(token.value + " " + msg)

    if __debug__:
        @staticmethod
        def print_server_msg(token, msg):
            print('cmd = ' + token.value)
            print('msg = ' + str(msg))

