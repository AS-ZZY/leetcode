class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []
        l = []
        level = [root]
        while len(level) != 0:
            ll = []
            a = len(level)
            b = 0
            for i in level:
                b += i.val
                if i.left is not None:
                    ll.append(i.left)
                if i.right is not None:
                    ll.append(i.right)
            l.append(b / a)
            level = ll
        return l