# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass

    def reverseLLIterativeWithMemory(self, head):
        """
        TC: O(N)
        SC: O(N)
        """
        stack, temp = [], head
        while temp:
            stack.append(temp)
            temp = temp.next
        
        head = temp = stack.pop()
        while len(stack) > 0:
            elem = stack.pop()
            temp.next = elem
            temp = elem
        
        elem.next = None
        return head
    
    def reverseLLRecursive(self, head):
        """
        TC: O(N)
        SC: O(N) due to stack 
        """
        if not head.next:
            return head
        
        rest = self.reverseLLRecursive(head.next)
        head.next.next = head
        head.next = None

        return rest
        
if __name__ == "__main__":
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    obj = Solution()
    #head = obj.reverseLLIterativeWithMemory(head)
    head = obj.reverseLLRecursive(head)
    while head:
        print(head.val)
        head = head.next