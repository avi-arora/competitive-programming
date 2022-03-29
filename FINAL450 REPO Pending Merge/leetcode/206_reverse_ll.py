# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverse LL using Recursion
        TC: O(N)
        SC: O(N) due to stack
        """

        if not head.next:
            return head
        else:
            node = self.reverseList(head.next)
            if node.next:
                head.next = node.next
            node.next = head
            return head

    def reverseListUsingStack(self, head: ListNode) -> ListNode:
        temp, s = head, []
        while temp:
            s.append(temp)
            temp = temp.next
        
        if len(s) > 0:
            temp = newHead = s.pop()
            while len(s) > 0:
                node = s.pop()
                temp.next = node
                temp = node
                #handle last node
                if(len(s) == 0):
                    node.next = None

            return newHead
        return head
    
    def reverseListNaive(self, head: ListNode) -> ListNode:
        pass
    



if __name__ == "__main__":
    obj = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    head = obj.reverseList(head)
    newHead = head.next
    head.next = None
    while newHead:
        print(newHead.val)
        newHead = newHead.next

        