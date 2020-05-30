class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def isSame(r1, r2):
            if r1 is None and r2 is None:
                return True
            elif r1 is None or r2 is None:
                return False
            if r1.val == r2.val:
                return isSame(r1.left, r2.right) and isSame(r1.right, r2.left)
            else:
                return False

        if not root:
            return True
        return isSame(root.left, root.right)