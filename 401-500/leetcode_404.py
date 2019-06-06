class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        if root is None:
            return 0
        if root.left is None:
            return self.sumOfLeftLeaves(root.right)
        else:
            if self.isleaf(root.left):
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        

    def isleaf(self, root):
        if root.left is None and root.right is None:
            return True
        else:
            return False