# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        listLen, curr = 0, head
        while curr: 
            listLen, curr = listLen+1, curr.next
        
        #reverse list till listLen/2
        counter = 0
        prev, curr = head, head.next if head and head.next else None
        
        tempPrev = prev
        while counter < (listLen // 2) -1 and curr:
            counter += 1
            nxt = curr.next
            
            curr.next = prev
            prev = curr
            curr = nxt
        
        # condition for edge case handling
        if listLen > 2:
            #update the prev to mid 
            tempPrev.next = nxt
            head = prev
        
        
        #traverse and find 
        maxPairSum = 0
        while curr:
            currPairSum = head.val + curr.val
            if currPairSum > maxPairSum:
                maxPairSum = currPairSum
            
            head = head.next 
            curr = curr.next 
        
        return maxPairSum
        
        
        
        