class LRU:

    def __init__(self, slots):
        self.slots = slots
        self.falts = 0
        self.list = []

    def add(self, value):
        if value not in self.list:
            self.falts += 1

        if len(self.list) >= self.slots:
            if value not in self.list:
                self.pop()
            else:
                self.pop(self.list.index(value))
        self.list.append(value)

    def pop(self, pos=None):
        if pos:
            self.list.pop(pos)
        else:
            self.list.pop(0)