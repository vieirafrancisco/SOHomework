import sys

from fifo import Fifo
from lru import LRU

def read_file(file_name):
    with open(file_name, "r") as f:
        result = map(lambda line: line.replace("\n",""), f.readlines())
    return result

if __name__ == "__main__":
    args = sys.argv
    slots = args[1]
    file_name = args[2]

    entries = read_file(file_name)
    fifo = Fifo(int(slots))
    lru = LRU(int(slots))

    for entrie in entries:
        fifo.add(int(entrie))
        lru.add(int(entrie))

    print(fifo.falts)
    print(lru.falts)