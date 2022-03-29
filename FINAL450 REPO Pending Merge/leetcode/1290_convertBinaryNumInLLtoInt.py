# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValueNaive(self, head: ListNode) -> int:
        if not head:
            return
        numStr = ""
        while head:
            numStr += str(head.val)
            head = head.next
        
        p = len(numStr)-1
        decimal = i = 0
        while p >= 0:
            decimal += int(numStr[i]) * pow(2,p)
            p-=1
            i+=1    
        return decimal


    def getDecimalValueBitManipulation(self, head: ListNode) -> int:
        if not head:
            return 
        
        decimal = head.val
        head = head.next
        while head:
            decimal = decimal << 1 | head.val
            head = head.next
        
        return decimal





if __name__ == "__main__":
    obj = Solution()
    head = ListNode(1,ListNode(0,ListNode(0,ListNode(1,ListNode(0,ListNode(0,ListNode(1,ListNode(1,ListNode(1,ListNode(0,ListNode(0,ListNode(0,ListNode(0,ListNode(0,ListNode(0)))))))))))))))
    print(obj.getDecimalValueNaive(head))
    print(obj.getDecimalValueBitManipulation(head))