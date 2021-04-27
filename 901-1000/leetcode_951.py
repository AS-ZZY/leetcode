class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False
        else:
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
