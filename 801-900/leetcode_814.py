class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode):
        def getNum(p):
            if not p:
                return 0
            else:
                left = getNum(p.left)
                right = getNum(p.right)
                if left == 0:
                    p.left = None
                if right == 0:
                    p.right = None
                return p.val + max(left, right)

        getNum(root)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
