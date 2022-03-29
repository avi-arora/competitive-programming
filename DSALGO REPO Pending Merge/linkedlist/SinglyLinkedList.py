from Node import SingleNode


class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
        self.tail = None

    def getData(self):
        return self.head.getData()
    
    def setData(self,elem):
        return self.head.setData(elem)

    def getNext(self):
        return self.head.getNext()

    def setNext(self, ptr):
        self.head.setNext(ptr)
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    
    def print(self):
        print("<<SinglyLinkedList>>")
        temp = self.head
        while temp:
            print(temp.getData(), end=" ")
            temp = temp.getNext()
        print()

    def insertAtFront(self, elem):
        node = SingleNode(elem)
        node.setNext(self.head)
        self.head = node

    def insertAtLast(self, elem):
        node = SingleNode(elem)
        temp = self.head
        if not self.head:
            self.head = node
        else:
            while temp.getNext():
                temp = temp.getNext()
            temp.setNext(node)

    def insertFront(self,elem):
        node = SingleNode(elem)
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            node.setNext(self.head)
            self.head = node

    def insertTail(self, elem):
        node = SingleNode(elem)
        #if list is empty 
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node


    def insertSorted(self, elem):
        pass

    def sort(self):
        pass


if __name__ == "__main__":
    pass
