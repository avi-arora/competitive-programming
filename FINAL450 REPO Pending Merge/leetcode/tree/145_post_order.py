# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversalRecurr(self, root: TreeNode) -> [int]:
        result = []
        def postOrderUtil(root):
            if root:
                postOrderUtil(root.left)
                postOrderUtil(root.right)
                result.append(root.val)
        postOrderUtil(root)
        return result

    def postOrderTraversalItrUsingTwoStack(self, root: TreeNode) -> [int]:
        """
        Algorithm
        1. use pre order traversal (root->right->left)
        2. reverse it's response and you'll get post order traversal
        TC:O(N)
        SC:O(N)
        """
        #step 1. iterative pre order traversal
        s = [root]
        res = []
        while len(s) > 0:
            n = s.pop()
            res.append(n.val)
            if n.left:
                s.append(n.left)
            
            if n.right:
                s.append(n.right)
        #step 2. reverse the response
        return res[::-1]
    
    def postOrderTraversalItrUsingOneStack(self, root: TreeNode) -> [int]:
        s = []
        r = []
        while True:

            while root:
                if root.right:
                    s.append(root.right)
                s.append(root)
                root = root.left
            
            root = s.pop()
            if root.right and len(s) > 0 and s[len(s)-1] == root.right:
                s.pop()
                s.append(root)
                root = root.right
            else:
                r.append(root.val)
                root = None
            
            if len(s) == 0:
                break
        return r

    def postOrderTraversalItrWithoutStack(self, root: TreeNode) -> [int]:
        pass
        
if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
    print(obj.postOrderTraversalItrUsingTwoStack(root))
    print(obj.postOrderTraversalItrUsingOneStack(root))
        