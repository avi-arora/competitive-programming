# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Accepted
        TC: O(N)
        SC: O(1) if consider recursive stack then O(N)
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        #imp step, could not perform seperately.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSameTreeItr(self, p:TreeNode, q: TreeNode) -> bool:
        """
        Accepted
        TC: O(N)
        SC: O(N)
        """
        if not q and not q: 
            return True
        q = [(p, q)]
        while len(q) > 0:
            n1, n2 = q.pop(0)

            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            if n1.left or n2.left:
                q.append((n1.left, n2.left))
            if n2.right or n2.right:
                q.append((n1.right, n2.right))
            
        
        return True

