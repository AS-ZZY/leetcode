class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        l = [root]
        re = []
        while len(l) != 0:
            re.append(l[-1].val)
            l = self.c_w(l)
        return re

    def c_w(self, l):
        t = []
        for i in l:
            if i.left is not None:
                t.append(i.left)
            if i.right is not None:
                t.append(i.right)
        return t
