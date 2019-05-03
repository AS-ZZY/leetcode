class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = self.leaf(root1)
        l2 = self.leaf(root2)
        return l1 == l2

    def leaf(self, root):
        l = []
        re = []
        p = root
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                if p.left is None and p.right is None:
                    re.append(p)
                p = p.right
            else:
                l.append(p)
                p = p.left
        return re


