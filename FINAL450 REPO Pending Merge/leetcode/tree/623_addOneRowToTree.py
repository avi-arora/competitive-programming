# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def levelOrderItr(self, root: TreeNode): 
        if not root:
            return 
        q, tq = [root], []
        lvl, nodePerLvl = 0, 0
        while len(q) > 0:
            n = q.pop(0)
            print(n.val)
            nodePerLvl += 1
            if n.left:
                tq.append(n.left)
            if n.right:
                tq.append(n.right)
            
            if len(q) == 0:
                lvl += 1
                nodePerLvl = 0
                q = tq
                tq = []
    
    
    def addOneRowDFS(self, root: TreeNode, v: int, d: int, ) -> TreeNode:
        def dfsUtil(root, v, d, n):
            if not root:
                return None
            #base case 
            if n == d-1:
                l, r = TreeNode(v, root.left), TreeNode(v, None,root.right)
                root.left, root.right = l, r
            else:
                dfsUtil(root.left, v, d, n+1)
                dfsUtil(root.right, v, d, n+1)
               # return root incorrect
        if d == 1:
            n = TreeNode(v, root)
            return n
        else:
            dfsUtil(root, v, d, 1)
            return root
            



    def addOneRowIncorrectSoln(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return root
        if d == 1:
            n = TreeNode(v,root)
            return n
        else:
            q, tq = [root], []
            nodePerLvl, lvl = 0, 0
            while len(q) and lvl < d-2:
                n = q.pop(0)
                nodePerLvl += 1
                if n.left:
                    tq.append(n.left)
                if n.right:
                    tq.append(n.right)
                
                if len(q) == 0:
                    lvl += 1
                    nodePerLvl = 0
                    q = tq
                    tq = []
            
            #create to nodes
            l, r = TreeNode(v), TreeNode(v)
            leftMostSubtree = q.pop(0) if len(q) > 0 else None
            rightMostSubtree = q.pop() if len(q) > 0 else None
            if leftMostSubtree:
                l.left = leftMostSubtree.left
                leftMostSubtree.left = l
            if not rightMostSubtree:
                r.right = leftMostSubtree.right
                leftMostSubtree.right = r
            else:
                r.right = rightMostSubtree.right
                rightMostSubtree.right = r
            
            return root
    



if __name__ == "__main__":
    root = TreeNode(4,TreeNode(2,TreeNode(3),TreeNode(5)), TreeNode(6,None,TreeNode(7)))
    obj = Solution()
    root = obj.addOneRowDFS(root,1,3)
    obj.levelOrderItr(root)
  