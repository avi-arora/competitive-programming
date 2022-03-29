# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        q, tq = [root], []
        levelSum = nodeCount = 0
        result = []
        while len(q) > 0:
            elem = q.pop(0)
            levelSum += elem.val
            nodeCount += 1

            if elem.left:
                tq.append(elem.left)
            if elem.right:
                tq.append(elem.right)
            
            if len(q) == 0:
                result.append(levelSum/nodeCount)
                levelSum = nodeCount = 0
                q = tq
                tq = []
        
        return result


if __name__ == "__main__":
    root = TreeNode(3,TreeNode(9), TreeNode(20,TreeNode(15), TreeNode(7)))
    obj = Solution()
    print(obj.averageOfLevels(root))

        