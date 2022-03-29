# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        using added dummy(sentinal) node
        TC: O(N)
        SC: O(1)
        """
        #add dummy node 
        node = ListNode(0, head)
        
        prev = head = node
        temp = head.next
        while temp and temp.next:
            curr = temp.next
            while curr and curr.val == temp.val:
                curr = curr.next
            if curr != temp.next:
                prev.next = curr
                temp = curr 
            else:
                prev = temp 
                temp = curr
        
        return head.next
        

if __name__ == "__main__":
    obj = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(3))))
    head = obj.deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next


        