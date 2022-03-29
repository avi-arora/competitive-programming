# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            return False
        
        ls, q = 0, [root]
        while len(q) > 0:
            e = q.pop(0)
            if e and e.left:
                if isLeaf(e.left):
                    ls+=e.left.val
                else:
                    q.append(e.left)
            if e and e.right:
                q.append(e.right)
        
        return ls


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20,TreeNode(15), TreeNode(7)))
    obj = Solution()
    print(obj.sumOfLeftLeaves(root))
        