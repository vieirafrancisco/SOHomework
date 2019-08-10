
class Opt:

    def __init__(self, slots, pages):
        self.slots = slots
        self.falts = 0
        self.list = []

        self.pages = pages
        self.falts_list = [[] for cont in range((max(pages)+1))]
        self.load()

    def load(self):
        for cont in range(len(self.pages)):
            self.falts_list[self.pages[cont]].append(cont)
        
        
    def add(self, value, index):
        founded = False
        last_page = None
        index_page = 0

        for l in self.list:
            if l == value:
                founded = True
             
            page_index_list = self.falts_list[l]

            while len(page_index_list) > 0 and index >= page_index_list[0]:
                page_index_list.pop(0)

            if len(page_index_list) == 0:
                last_page = (index_page, 0)
            elif last_page != None:
                if last_page[1] != 0 and page_index_list[0] > last_page[1]:
                    last_page = (index_page, page_index_list[0])
            elif last_page == None:
                last_page = (index_page, page_index_list[0])
            
            index_page+=1


        if not founded:
            self.falts += 1
            if len(self.list) == self.slots:
                self.list.pop(last_page[0])

            self.list.append(value)
        
