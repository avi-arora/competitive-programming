from SinglyLinkedList import SinglyLinkedList


def reverseNaive(list: SinglyLinkedList):
    """
    using insert at front technique

    TC: O(n)
    SC: O(n) -  not so good

    """
    result, temp = SinglyLinkedList(), list
    while temp:
        result.insertAtFront(temp.getData())
        temp = temp.getNext()
    
    return result

def reverseUsingStack(list: SinglyLinkedList):
    """
    using stack push and pop operations
    TC: O(n)
    SC: O(n) - not improved
    """
    stack, temp = [], list
    while temp: 
        stack.append(temp.getData())
        temp = temp.getNext()

    temp = list
    while temp:
        temp.setData(stack.pop())
        temp = temp.getNext()
    
    return list

def reverseImproved(list: SinglyLinkedList):
    """
    TC: O(n)
    SC: O(1)
    """
    temp, prev, current = list.getNext(), list, list.getNext()
    while current:
        temp = temp.getNext()
        current.setNext(prev)
        prev = current 
        current = temp
    list.setNext(None)
    return SinglyLinkedList(prev)
         

def reverseRecursive(head, current, prev):
    """
    TC: O(n)
    SC: O(n)
    """
    if not current.getNext():
        current.setNext(prev)
        return current
    else:
        newHead = reverseRecursive(head, current.getNext(), current)
        current.setNext(prev)
        if prev == head:
            prev.setNext(None)
            return SinglyLinkedList(newHead)
        return newHead




if __name__ == "__main__":

    list = SinglyLinkedList()
    list.insertAtLast(1)
    list.insertAtLast(2)
    list.insertAtLast(3)
    list.insertAtLast(4)
    list.insertAtLast(5)

    list.print()
    rev = reverseRecursive(list, list.getNext(), list)
    rev.print()
    
