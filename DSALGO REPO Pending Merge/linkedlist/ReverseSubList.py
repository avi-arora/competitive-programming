from SinglyLinkedList import SinglyLinkedList
from Node import SingleNode


def reverseSublistNaive(list: SinglyLinkedList, start, end):
    """
    Algorithm: Create a new list for the sublist in reverse order,
    by using InsertAtFront Operation 
    TC: O(end), in worst case O(n)
    SC: O((end-start)+1), in worst case O(n)
    """
    assert end > start, "End should be greater than start"
    result = SinglyLinkedList()
    head = None
    prev, curr, counter = None, list, 1

    while counter < start and curr:
        prev, curr = curr, curr.getNext()
        counter += 1

    head = prev if prev else list

    while counter <= end and curr:
        result.insertFront(curr.getData())
        prev, curr = curr, curr.getNext()
        counter += 1

    if start == 1:
        return result
    else:
        head.setNext(result)
        result.getTail().setNext(curr)

    return list


def reverseSublistNaiveImproved(head: SingleNode, start, end):
    assert end > start, "End should be greater than start"
    pass


def reverseSublistUsingStack(list: SinglyLinkedList, start, end):
    assert end > start, "End should be greater than start"
    prev, curr = None, list
    stack, counter = [], 1

    while counter < start and curr:
        prev, curr, counter = curr, curr.getNext(), counter + 1

    while counter <= end and curr:
        stack.append(curr.getData())
        curr, counter = curr.getNext(), counter+1

    curr, counter = prev.getNext() if prev else list, start
    while counter <= end and curr and stack:
        curr.setData(stack.pop())
        curr, counter = curr.getNext(), counter+1

    return list


def reverseSublistImproved(list: SinglyLinkedList, start, end):
    assert end > start, "End should be greater than start"
    prev, curr, temp = None, list, list
    counter, subListHead = 1, None

    #traverse till position 
    while counter < start and curr:
        prev, curr = curr, curr.getNext()
        counter += 1
    
    subListHead = prev if prev else list
    #position obtained start reversing
    while counter <= end and temp:
        temp = curr.getNext()
        curr.setNext(prev)
        prev, curr = curr, temp
        counter += 1

    #reversal successful 
    #this indicate the reversal is starting from beganning 
    if not subListHead.getNext() and not curr:
        list = SinglyLinkedList(prev)
    elif not subListHead.getNext():
        subListHead.setNext(curr)
        list = SinglyLinkedList(prev)
    else:
        subListHead.getNext().setNext(curr)
        subListHead.setNext(prev)

    return list


def reverseRecursive(list: SinglyLinkedList, start, end):
    assert end > start, "End should be greater than start"
    pass


if __name__ == "__main__":
    l = SinglyLinkedList()

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

    result = reverseSublistImproved(l, 1, 7)

    result.print()
