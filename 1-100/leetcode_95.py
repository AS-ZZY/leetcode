class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        res = []
        if n < 1:
            return res
        else:
            return self.generateBST(1, n)
        
    def generateBST(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        else:
            for i in range(start, end + 1):
                left_tree = self.generateBST(start, i - 1)
                right_tree = self.generateBST(i + 1, end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res