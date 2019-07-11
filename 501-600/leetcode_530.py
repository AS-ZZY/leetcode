class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode):
        l = []
        p = root
        frist = float("-inf")
        m = float("inf")
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                mu = abs(p.val - frist)
                frist = p.val
                if m > mu:
                    m = mu
                p = p.right
            else:
                l.append(p)
                p = p.left
        return m
                
                