# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = head, head.next if head and head.next else None
        
        # Edge # if list only contains single node
        if not curr:
            return head
        
        #set the new end
        prev.next = None
        while curr:
            nxt = curr.next
            
            #change links
            curr.next = prev
            prev = curr
            curr = nxt 
        
        
        return prev
