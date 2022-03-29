class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        
        pos = 0
        temp = self.head
        while pos < index and temp:
            temp = temp.next
            pos+=1
        
        if pos == index and temp:
            return temp.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        #if list is empty
        if not self.head:
            self.head = newNode
        else:
            #traverse till end 
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        pos = 0
        prev = None
        temp = self.head
        while pos < index and temp.next:
            pos += 1
            prev = temp 
            temp = temp.next
        
        if pos == index and temp:
            newNode = Node(val)
            #handle for one node
            if prev == self.head:
                newNode.next = self.head
                self.head = newNode
            else:
                newNode.next = prev.next
                prev = newNode
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        pos = -1
        prev = None
        temp = self.head
        while pos+1 <= index and temp.next:
            prev = temp
            temp = temp.next
            pos += 1
        
        if pos <= index and temp.next:
            prev.next = temp.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next



if __name__ == "__main__":
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
# param_1 = obj.get(index)
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1,2)
    obj.print()
# obj.deleteAtIndex(index)