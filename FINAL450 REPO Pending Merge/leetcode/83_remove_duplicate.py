# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesBruteForce(self, head: ListNode) -> ListNode:
        """
        Remove Duplicate from sorted linked list using brute force naive algorithm.
        TC: O(N)
        SC: O(1)

        """
        temp = head
        while temp and temp.next:
            curr = temp.next
            while curr and curr.val == temp.val:
                curr = curr.next
            temp.next = curr
            temp = curr
        
        return head



if __name__ == "__main__":
    # import doctest
    # doctest.testmod(extraglobs={'t': Solution()})
    head = ListNode(1,ListNode(2,ListNode(2,ListNode(2,ListNode(3)))))
    obj = Solution()
    obj.deleteDuplicatesBruteForce(head)

    while head:
        print(head.val)
        head = head.next


        