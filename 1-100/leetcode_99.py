class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        p = root
        l = []
        vals = []
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                vals.append(p)
                p = p.right
            else:
                l.append(p)
                p = p.left
        if len(vals) == 0:
            return None
        for i in range(len(vals) - 1):
            if vals[i].val > vals[i + 1].val:
                global p1
                p1 = vals[i]
                break
        for i in range(len(vals) - 1, -1, -1):
            if vals[i].val < vals[i - 1].val:
                global p2
                p2 = vals[i]
                break
        a = p1.val
        p1.val = p2.val
        p2.val = a


