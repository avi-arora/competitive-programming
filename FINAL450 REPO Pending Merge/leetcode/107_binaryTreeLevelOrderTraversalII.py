# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        q, tq = [root], []
        r, temp = [], []
        
        while len(q) > 0:
            e = q.pop(0)
            temp.append(e.val)
            
            if e.left:
                tq.append(e.left)
            if e.right:
                tq.append(e.right)
            
            if len(q) == 0:
                r = [temp] + r
                temp = []
                q = tq
                tq = []
        
        return r
            
        