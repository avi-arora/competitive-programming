from SinglyLinkedList import SinglyLinkedList

def kReverse(list: SinglyLinkedList, k):
    if k <= 1:
        return list

    


def kReverseRecursive(list: SinglyLinkedList, k):
    pass


    def revSubList(list: SinglyLinkedList, k):
        """
        reverse the list and returns head and tail 
        """
        pass




if __name__ == "__main__":
    l = SinglyLinkedList()

    l.insertAtFront(10)
    l.insertAtFront(9)
    l.insertAtFront(8)
    l.insertAtFront(7)
    l.insertAtFront(6)
    l.insertAtFront(5)
    l.insertAtFront(4)
    l.insertAtFront(3)
    l.insertAtFront(2)
    l.insertAtFront(1)

    l.print()

    kReverse(l, 2)

    l.print()

