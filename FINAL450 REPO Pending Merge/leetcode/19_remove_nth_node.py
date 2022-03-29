# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Remove nth node from end of LL in one pass, without extra space
        two pointer approach, (not to confused with slow-fast ptr approach)
        Algorithm
        1. place the fast pointer n steps ahead of start from LL
        2. iterate both temp and fast will fast.next is non empty (this will place the temp before the n node)
        3. update temp (head in case of corner cases)
        TC: O(N)
        SC: O(1)
        """
        temp = fast = head
        #place the fast to it's position
        i = 0
        while i < n:
            fast = fast.next
            i+=1
        
        #move fast and temp 
        while fast and fast.next:
            temp, fast = temp.next, fast.next
        
        if fast: 
            temp.next = temp.next.next
        else:
            head = head.next

        return head
    
    def removeNthFromEndUsingStack(self, head: ListNode, n: int) -> ListNode:
        """
        Removed nth node using stack, only in one pass
        ACCEPTED
        TC: O(N)
        SC: O(N)
        """
        #fill the stack
        s, temp = [], head
        while temp:
            s.append(temp)
            temp = temp.next
        
        #pop n-1 elem from stack and store the prev 
        i,elem = 0, None
        while i < n:
            elem = s.pop()
            i+=1
        if len(s) > 0:
            t = s.pop()
            t.next = elem.next
        else:
            head = head.next
        return head

    def removeNthFromEndTwoPass(self, head: ListNode, n: int) -> ListNode:
        """
        Remove nth node from the end of ll, using two pass technique
        algorithm 
        1. compute length of ll using iteration
        2. traverse till len(ll) - n them apply removal 

        TC: O(n)
        SC: O(1)
        """
        Llen, temp = 0, head
        while temp:
            temp, Llen = temp.next, Llen+1
        temp,pos = head, 0
        if pos == Llen - n:
            head = temp.next
        else:
            while pos < (Llen - n)-1:
                temp, pos = temp.next, pos+1
            if temp.next and temp.next.next:
                temp.next = temp.next.next
            else:
                temp.next = None

        return head

        


if __name__ == "__main__":
    l = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    obj = Solution()
    t = obj.removeNthFromEndUsingStack(l,5)
    while t:
        print(t.val)
        t = t.next
