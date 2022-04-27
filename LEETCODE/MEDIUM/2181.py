# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        current = head 
        while current and current.next: 
            lineSum, temp = 0, current.next
            
            while temp and temp.val != 0:
                lineSum += temp.val
                temp = temp.next
            
            current.val = lineSum
            current.next = temp if temp.next else None
            current = temp
            
        return head
        