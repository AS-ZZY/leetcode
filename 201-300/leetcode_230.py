class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        i = 0
        l = []
        p = k
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                i += 1
                if i == k:
                    return p.val
                p = p.right
            else:
                l.append(p)
                p = p.left