class Node(object):
    def __init__(self, father, coord, level, level2=None):
        self.father   = father
        self.coord    = coord
        self.level    = level
        self.level2   = level2
        self.previous = None
        self.next     = None