# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodesNaive(self, head: ListNode, k: int) -> ListNode:
        len, temp = 0, head
        while temp:
            len, temp = len+1, temp.next
        
        itrRight = itrLeft = head
        #position the iterators
        i = 1
        while i < k:
            itrRight = itrRight.next
            i+=1
        
        i = 1
        while i <= len-k:
            itrLeft = itrLeft.next
            i+=1
        
        #swap data
        itrRight.val, itrLeft.val = itrLeft.val, itrRight.val


    def swapNodesEfficient(self, head: ListNode, k: int) -> ListNode:
        if not head: return 
        temp,i = head, 1
        while i < k:
            temp = temp.next
            i+=1
        
        left, right = temp, head
        while temp:
            temp = temp.next
            right = right.next
        
        left.val, right.val = right.val, left.val

        return head

            
        


if __name__ == "__main__":
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    obj = Solution()
    obj.swapNodesNaive(head, 2)
    while head:
        print(head.val)
        head = head.next
        