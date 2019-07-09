class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode):
        p = root
        l = []
        front = 0
        frist = False
        min1 = float("inf")
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                if not frist:
                    frist = True
                else:
                    if min1 > p.val - front:
                        min1 = p.val - front
                front = p.val
                p = p.right
            else:
                l.append(p)
                p = p.left
        return min1