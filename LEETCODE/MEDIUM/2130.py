# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        """
        Solution 1
        TC: O(n)
        SC: O(n)
        """
        tempList, current = [], head
        while current:
            tempList.append(current.val)
            current = current.next
        
        maxTwinSum = tempList[0] + tempList[len(tempList)-1]
        start, end = 1, len(tempList)-2
        while start < end:
            currentTwinSum = tempList[start] + tempList[end]
            if currentTwinSum > maxTwinSum:
                maxTwinSum = currentTwinSum
                
            start, end = start+1, end-1
        
        return maxTwinSum

    def pairSumUsingStack(self, head) -> int:
        listLen, curr = 0, head
        while curr:
            listLen += 1
            curr = curr.next
        
        stack = []
        i, curr = 0, head 
        while i < (listLen//2):
            stack.append(curr.val)
            curr, i = curr.next, i+1
        
        maxPairSum = stack.pop() + curr.val
        curr = curr.next
        while curr:
            currentPairSum = stack.pop() + curr.val
            if currentPairSum > maxPairSum:
                maxPairSum = currentPairSum
            
            curr = curr.next
        
        return maxPairSum

    