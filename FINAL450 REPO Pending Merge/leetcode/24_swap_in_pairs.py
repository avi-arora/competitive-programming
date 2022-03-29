# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        curr, next = head, head.next if head else None
        resultHead = head.next if head and head.next else head
        while next:
            if prev:
                prev.next = next
            #swap
            curr.next = next.next 
            next.next = curr
            #update
            prev = curr
            curr = curr.next
            next = curr.next if curr else None
        
        return resultHead
        

if __name__ == "__main__":
    head = ListNode(1)#ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, ListNode(6))))))
    obj = Solution()
    head = obj.swapPairs(head)
    while head:
        print(head.val)
        head = head.next


        