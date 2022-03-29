from SinglyLinkedList import SinglyLinkedList


def hasCycle(list: SinglyLinkedList):
    """
    Detect a cycle using floyd 2 pointer approach
    TC: O(n)
    SC: O(1)
    """
    slow = fast = list
    while fast and fast.getNext() and fast.getNext().getNext():
        slow, fast = slow.getNext(), fast.getNext().getNext()
        if slow is fast:
            return 1
    return 0


def hasCycleMemory(list: SinglyLinkedList):
    """
    uses hash table to check the cycle
    TC: O(n)
    SC: O(n)
    """
    visited, curr = {}, list
    while curr:
        if curr in visited:
            return 1
        visited[curr], curr = curr.getData(), curr.getNext()

    return 0


def hasCycleWithLength(list: SinglyLinkedList):
    """
    Returns the length of the cycle if any
    TC: O(n)
    SC: O(1)
    """
    slow = fast = list
    isCyclic = False
    while fast and fast.getNext() and fast.getNext().getNext():
        slow, fast = slow.getNext(), fast.getNext().getNext()
        if slow is fast:
            # overlapping detected, i.e cycle exits
            isCyclic = True
            break

    cycleLen = 0
    if isCyclic:
        slow = slow.getNext()
        while slow is not fast:
            cycleLen, slow = cycleLen + 1, slow.getNext()

    return cycleLen

def hasCycleWithLocation(list: SinglyLinkedList):
    """
    Returns the node where the cycle began
    TC: O(n)
    SC: O(1)
    """
    #detect a cycle
    slow = fast = list
    isCyclic = False
    while fast and fast.getNext() and fast.getNext().getNext():
        slow, fast = slow.getNext(), fast.getNext().getNext()
        if slow is fast:
            isCyclic = True
            break
    
            

def hasCycleBruteForce(list: SinglyLinkedList):
    pass


if __name__ == "__main__":
    l = SinglyLinkedList()

    l.insertAtFront(5)
    l.insertAtFront(4)
    l.insertAtFront(3)
    l.insertAtFront(2)
    l.insertAtFront(1)

    l.print()

    # modify list to create a cycle
    #l.getNext().getNext().getNext().setNext(l.getNext())

  #  l.print()

    print(hasCycleWithLength(l))
