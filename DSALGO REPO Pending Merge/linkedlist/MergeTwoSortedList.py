from SinglyLinkedList import SinglyLinkedList
from Node import SingleNode


def MergeSortedLinkedList(S1: SinglyLinkedList, S2: SinglyLinkedList):
    if S1 and S2:
        result = SinglyLinkedList()
        while S1 and S2:
            if S1.getData() < S2.getData():
                result.insertTail(S1.getData())
                S1 = S1.getNext()
            else:
                result.insertTail(S2.getData())
                S2 = S2.getNext()

        while S1:
            result.insertTail(S1.getData())
            S1 = S1.getNext()

        while S2:
            result.insertTail(S2.getData())
            S2 = S2.getNext()

        return result

#very important improved version
def MergeSortedLinkedListImproved(S1: SinglyLinkedList, S2: SinglyLinkedList):
    result = temp = SingleNode()

    while S1 and S2:
        if S1.getData() < S2.getData():
            temp.setNext(S1)
            S1 = S1.getNext()
        else:
            temp.setNext(S2)
            S2 = S2.getNext()
        #optimization factor
        temp = temp.getNext()
    
    #if S1:
    #    temp.setNext(S1)
    #else:
    #    temp.setNext(S2)

    #further optimization
    temp.setNext(S1 or S2)
    
    return result.getNext()

if __name__ == "__main__":
    l1, l2 = SinglyLinkedList(), SinglyLinkedList()

    l1.insertAtFront(10)
    l1.insertAtFront(5)
    l1.insertAtFront(1)

    l2.insertAtFront(20)
    l2.insertAtFront(4)
    l2.insertAtFront(0)

    l1.print()
    l2.print()

   # res = MergeSortedLinkedList(l1, l2)

    #res.print()\

    res = MergeSortedLinkedListImproved(l1,l2)

    temp = res
    while res:
        print(res.getData(), end=" ")
        res = res.getNext()

    

    


    
    
