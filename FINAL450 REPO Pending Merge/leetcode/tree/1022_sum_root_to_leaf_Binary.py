# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inOrderRecurr(self, root: TreeNode):
        if root:
            self.inOrderRecurr(root.left)
            print(root.val)
            self.inOrderRecurr(root.right)
        
    def inOrderItr(self, root: TreeNode):
        s = []
        curr = root
        while True:
            #put right subtree in stack
            while curr:
                s.append(curr)
                curr = curr.left
            
            if not curr and len(s) > 0:
                n = s.pop()
                print(n.val)
                curr = n.right
            
            if not curr and len(s) == 0:
                break
    
    def preOrderRecurr(self, root: TreeNode):
        if root:
            print(root.val)
            self.preOrderRecurr(root.left)
            self.preOrderRecurr(root.right)
    
    def preOrderItr(self, root:TreeNode):
        s = [root]
        while len(s) > 0:
            n = s.pop()
            print(n.val)
            #right is first due to stack LIFO, left should pop first.
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)
            
    def postOrderItr(self, root: TreeNode): 
        q = [root]:
        while len(q) > 0:
               

    def sumRootToLeaf(self, root: TreeNode) -> int:
        pass

    def sumRootToLeafDecimal(self, root: TreeNode) -> int: 
        pass


if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(3,TreeNode(1), TreeNode(2))
    #obj.inOrderItr(root)
    #obj.inOrderRecurr(root)
    obj.preOrderRecurr(root)




        