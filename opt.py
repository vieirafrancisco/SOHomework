
class Opt:

    def __init__(self, slots, pages):
        self.slots = slots
        self.falts = 0
        self.pages = pages
        self.falts_list = max(pages)*[0]
        self.load()

    def load(self):
        for page in self.pages:
            self.falts_list[page] += 1

    def add(self):
        pass


class Page:

    def __init__(self, page_id, rec):
        self.page_id = page_id
        self.rec = rec

    def __gt__(self, other):
        return self.rec < other.rec

class OrderedList:

    def __init__(self, page_list):
        self.list = sorted(page_list)

    def add(self, page):
        page_idx = self.search(page.rec)
        self.list.insert(page_idx)

    def search(self, rec):
        begin = 0
        end = len(self.list)-1

        while (begin <= end):
            mid = (begin+end)//2

            if self.list[mid] == rec:
                return (mid, True)
            elif self.list[mid] < rec:
                if(self.list[mid+1] > rec):
                    return (mid, False)
                begin = mid+1
            else:
                end = mid-1
        return (mid, False)
        