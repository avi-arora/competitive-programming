# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
     def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
         pass
    
     def mergeTwoListsCodeImproved(self, l1: ListNode, l2: ListNode) -> ListNode:
         pass
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = temp = None
        while l1 and l2:
            if l1.val < l2.val:
                if temp:
                    temp.next = l1
                    temp = l1
                else:
                    result = temp = l1
                l1 = l1.next
            else:
                if temp: 
                    temp.next = l2
                    temp = l2
                else:
                    result = temp = l2
                l2 = l2.next
        if l1:
            if temp:
                temp.next = l1
            else:
                result = temp = l1
        if l2:
            if temp:
                temp.next = l2
            else:
                result = temp = l2
            
        return result
                