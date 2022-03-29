#problem link: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodeNaive(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        TC: O(N) precisely O(N) - length till node
        SC: O(1)
        """
        prev, temp = None, node
        while temp.next:
            temp.val = temp.next.val
            prev = temp
            temp = temp.next
        prev.next = None
    
    def deleteNodeEfficient(self, node):
        """
        TC: O(1)
        SC: O(1)
        """
        node.val = node.next.val
        node.next = node.next.next
        
if __name__ == "__main__":
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    tempHead = head.next.next.next
    obj = Solution()
    obj.deleteNodeEfficient(tempHead)
    while head:
        print(head.val)
        head = head.next