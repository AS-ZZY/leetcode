class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0
        self.getVal(root, 0)
        return self.sum % (10 ** 9 + 7)

    def getVal(self, root, val):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.sum += val * 2 + root.val
            return
        self.getVal(root.left, val * 2 + root.val)
        self.getVal(root.right, val * 2 + root.val)