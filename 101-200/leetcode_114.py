class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode):
        if root is None:
            return root
        s = []
        l = root
        p = []
        while len(p) != 0 or l is not None:
            if l is not None:
                s.append(l)
                p.append(l)
                l = l.left
            else:
                l = p.pop().right
        for i in range(len(s) - 1):
            s[i].left = None
            s[i].right = s[i + 1]
        s[-1].left = None
        s[-1].right = None
            

        



