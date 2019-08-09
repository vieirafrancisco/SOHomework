class LRU:

    def __init__(self, slots):
        self.slots = slots
        self.falts = 0
        self.list = []

    def add(self, value):
        f = value in self.list
        if not f:
            self.falts += 1
        else:
            self.list.pop(self.list.index(value))

        if len(self.list) == self.slots and not f:
            self.list.pop(0)
 
        self.list.append(value)