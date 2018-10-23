
class AI:
    def __init__(self, id, board):
        self.id = id
        self.board = board

    def do_command(self, command, parameters):
        attr_name = "cmd_" + command.value
        try:
            self.__getattribute__(attr_name)(parameters)
        except Exception:
             print(f'Command \"{command.value}\" not yet implemented.')

