class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        n = []
        for i in self.qlist:
            n.append(i.priority)
        print (self.qlist.pop(n.index(min(n))).item)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


lut = PriorityQueue()
lut.enqueue('Pak Rt', 4)
lut.enqueue('Mbah Uti', 2)
lut.enqueue('Mbah Darjo', 0)
lut.enqueue('Cah Cilik', 5)
lut.enqueue('Pak Lurah', 3)

lut.dequeue()
lut.dequeue()
lut.dequeue()
lut.dequeue()
lut.dequeue()
