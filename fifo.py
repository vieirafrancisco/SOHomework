class Fifo:

    def __init__(self, slots):
        self.slots = slots
        self.falts = 0
        self.list = []

    def add(self, value):
        if value not in self.list:
            if len(self.list) >= self.slots:
                self.pop()
            self.list.append(value)
            self.falts += 1

    def pop(self):
        self.list.pop(0)
