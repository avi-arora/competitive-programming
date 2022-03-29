
#Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorderRecur(self, root: 'Node') -> [int]:
        if not root: return []
        r = []
        def postOrderUtil(root):
            if root:
                if root.children:
                    for c in root.children:
                        postOrderUtil(c)
                r.append(root.val)
        
        postOrderUtil(root)
        return r
    
    def postorderItr(self, root: Node) -> []:
        pass


            
        