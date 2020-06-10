class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        l = [root]
        result = []
        while len(l) > 0:
            p = l[0]
            result.append(p.val)
            if p.left:
                l.append(p.left)
            if p.right:
                l.append(p.right)
            l = l[1:]
        return result