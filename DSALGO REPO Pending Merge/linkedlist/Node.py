
class SingleNode: 
    
    def __init__(self,elem=None):
        self.data, self.next = elem, None

    
    def setData(self, val):
        self.data = val
    
    def setNext(self, ptr):
        self.next = ptr

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class DoubleNode(SingleNode):

    def __init__(self):
        SingleNode.__init__(self)
        self.prev = None

    def setPrev(self, ptr):
        self.prev = ptr

    def getPrev(self):
        return self.prev

