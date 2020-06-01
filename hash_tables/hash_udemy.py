class Hashtable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size