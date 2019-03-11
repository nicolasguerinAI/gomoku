from sys import maxsize

class Node(object):
    def __init__(self, i_depth, i_playernb, posx, posy, i_value = 0):
        self.i_depth = i_depth
        self.i_playernb = i_playernb
        self.posx = posx
        self.posy = posy
        self.i_value = i_value
        self.children = []
        self.CreateChildren()


    def CreateChildren(self):
        if self.i_depth >= 0:
            for i in range(1, 3):
                new_posx = 0
                new_posy = 0
                self.children.append(Node(self.i_depth - 1, -self.i_playernb, new_posx, new_posy))

