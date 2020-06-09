class Queue():
    def __init__(self):
        self.lst = []
    def Addtoqueue(self, item):
        self.lst.append(item)
        print(self.lst)
    def Popfromqueue(self, item):
        self.lst.pop(0)
        print(self.lst)
    def Sizeofqueue(self):
        size=len(self.lst)
        print(size)

newItem = Queue()
newItem.Addtoqueue("test")
newItem.Popfromqueue("test")
newItem.Sizeofqueue()
