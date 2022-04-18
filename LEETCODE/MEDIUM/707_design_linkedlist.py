class Node:
    def __init__(self, val):
        self.next, self.val = None, val

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= 0:
            currentNode, currentIndex = self.head, 0
            while currentNode and currentNode.next != None and currentIndex < index:
                currentNode = currentNode.next
                currentIndex += 1
            
            if currentIndex == index and currentNode:
                return currentNode.val
            else:
                return -1
               
        return -1
        

    def addAtHead(self, val: int) -> None:
        #list is empty
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= 0:
            #traverse till index
            if index == self.length: 
                self.addAtTail(val)
            elif index == 0:
                self.addAtHead(val)
            else:
                previousNode, currentNode, currentIndex = None, self.head, 0
                while currentNode and currentNode.next != None and currentIndex < index:
                    previousNode = currentNode
                    currentNode = currentNode.next
                    currentIndex += 1
                
                if currentIndex == index:
                    if previousNode and currentNode:
                        newNode = Node(val)
                        newNode.next = currentNode
                        previousNode.next = newNode
                    elif currentNode and not previousNode:
                        newNode = Node(val)
                        newNode.next = currentNode.next
                        self.head = newNode
                self.length += 1
                
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and self.head:
            previousNode, currentNode = None, self.head
            currentIndex = 0
            while currentNode and  currentNode.next and currentIndex < index:
                previousNode = currentNode
                currentNode = currentNode.next
                currentIndex += 1
            
            if currentIndex == index:
                #list only contains one element
                if not previousNode and currentNode:
                    self.head = self.head.next 
                    #or self.head = currentNode.next
                elif previousNode and currentNode:
                    previousNode.next = currentNode.next
                self.length -= 1
                   
    def pl(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next

if __name__ == "__main__":
    ll = MyLinkedList()

    #operations
    ll.addAtHead(2)
    ll.addAtIndex(0, 1)
    ll.pl()
    print()
    print(ll.get(1))



    # ll.addAtHead(55)
    # ll.addAtIndex(1, 90)
    # ll.addAtTail(51)
    # ll.addAtTail(91)
    # ll.addAtTail(12)
    # ll.addAtIndex(2, 72)
    # ll.addAtTail(17)
    # ll.addAtHead(82)
    # ll.deleteAtIndex(4)
    # ll.deleteAtIndex(7)
    # ll.deleteAtIndex(7)

    # ll.addAtIndex(5,75)
    # ll.addAtTail(54)
    # ll.pl()
    # print()
    # print(ll.get(6))

    # ll.get(2)

    # ll.addAtHead(8)
    # ll.addAtTail(35)
    # ll.addAtTail(36)
    # ll.get(10)
    # ll.addAtTail(40)
    # ll.addAtTail(43)

    # ll.deleteAtIndex(12)
    # ll.deleteAtIndex(3)

    # ll.addAtHead(78)
    # ll.addAtTail(89)
    # ll.addAtIndex(3, 41)

    # ll.get(10)
    # ll.addAtTail(96)
    # ll.addAtIndex(5,37)
    # ll.addAtHead(51)
    # ll.addAtTail(26)
    # ll.addAtIndex(16, 91)
    # ll.get(18)
    # ll.addAtHead(11)
    # ll.addAtTail(66)
    # ll.addAtIndex(22,20)

    # ll.addAtHead(44)
    # ll.addAtIndex(17,16)
    # ll.addAtTail(95)
    # ll.addAtHead(2)
    # ll.addAtIndex(14,2)
    # ll.addAtTail(99)
    # ll.addAtHead(51)
    # ll.deleteAtIndex(1)

    # ll.get(11)
    # ll.addAtIndex(22,99)


    # ll.get(20)
    # ll.addAtIndex(25,42)
    # ll.addAtTail(72)
    # ll.addAtTail(45)
    # ll.get(2)
    # ll.deleteAtIndex(4)
    # ll.get(32)
    # ll.addAtHead(55)
    # ll.addAtTail(84)
    # ll.addAtIndex(32,64)
    # ll.addAtIndex(26,14)
    # ll.addAtIndex(30,80)
    # ll.addAtHead(88)
    # ll.addAtTail(51)
    # ll.addAtIndex(27,71)
    # ll.deleteAtIndex(15)
    # ll.addAtHead(8)
    # ll.addAtHead(60)
    # ll.addAtTail(37)
    # ll.get(25)
    # ll.addAtTail(96)
    # ll.addAtIndex(25,53)
    # ll.addAtHead(36)
    # ll.deleteAtIndex(8)
    # ll.addAtHead(85)
    # ll.deleteAtIndex(42)
    # ll.get(20)
    
    # ll.pl()
    # print()
    # print(ll.get(34))
    
    
    
    
    # ll.addAtTail(78)
    # ll.addAtIndex(42,76)
    # ll.get(26)
    # ll.deleteAtIndex(30)
    # ll.deleteAtIndex(39)
    # ll.addAtHead(27)
    # ll.addAtHead(93)
    # ll.addAtIndex(19,75)
    # ll.get(8)
    # ll.addAtTail(24)
    # ll.addAtHead(32)
    # ll.addAtIndex(25,98)
    # ll.get(21)
    # ll.addAtHead(95)
    # ll.deleteAtIndex(18)
    # ll.deleteAtIndex(45)
    # ll.deleteAtIndex(24)
    # ll.addAtHead(38)
    # ll.addAtTail(8)
    # ll.get(20)
    # ll.addAtHead(83)
    # ll.addAtTail(71)
    # ll.addAtHead(78)
    # ll.addAtHead(55)
    # ll.deleteAtIndex(29)
    # ll.get(11)
    # ll.addAtHead(84)







