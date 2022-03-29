# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBSTusingLevelOrderTraversal(self, root: TreeNode, low: int, high: int) -> int:
        """
        TC: O(N)
        SC: O(N)
        Status: Accepted
        """
        #do level order traversal concept and count result 
        rangeSum = 0
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            if node.val >= low and node.val <= high:
                rangeSum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return rangeSum
    
    def rangeSumBSTusingBFS(self, root: TreeNode, low: int, high: int) -> int:
        """
        TC: O(N)
        SC: O(N)
        """
        rangeSum = 0
        s = [root]
        while s:
            node = s.pop()
            if node.val >= low and node.val <= high:
                rangeSum += node.val
            
            if  node.val > low and node.left:
                s.append(node.left)
            if node.val < high and node.right:
                s.append(node.right)
        return rangeSum
    
    def rangeSumBSTusingDFSRecursive(self, root: TreeNode, low: int, high: int) -> int:
        """
        TC: O(N)
        SC: O(N) due to recursion
        Status: Accepted (best)
        """
        rangeSum = 0
        def DFSUtil(root: TreeNode):
            nonlocal rangeSum
            if root:
                if root.val >= low and root.val <= high:
                    rangeSum += root.val
                
                if root.val > low and root.left:
                    DFSUtil(root.left)
                if root.val < high and root.right:
                    DFSUtil(root.right)

        DFSUtil(root)
        return rangeSum
        

            
if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(10,TreeNode(5,TreeNode(3),TreeNode(7)),TreeNode(15,right=TreeNode(18)))
    print(obj.rangeSumBSTusingLevelOrderTraversal(root,7,15))
    print(obj.rangeSumBSTusingBFS(root, 7, 15))
    print(obj.rangeSumBSTusingDFSRecursive(root,7,15))
        