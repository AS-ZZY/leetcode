class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode):
        rootNew = TreeNode(0)
        r = rootNew
        l, t = [], root
        while t or len(l) > 0:
            if not t:
                t = l.pop()
                r.right = t
                t, r = t.right, r.right
                r.left = None
            else:
                l.append(t)
                t = t.left
        return rootNew.right
