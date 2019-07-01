class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        p = root
        l = []
        a = 0
        while p is not None or len(l) != 0:
            if p is not None:
                l.append(p)
                p = p.right
            else:
                p = l.pop()
                p.val += a
                a = p.val
                p = p.left
        return root  