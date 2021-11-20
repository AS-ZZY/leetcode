class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode):
        val, l, p = 0, [], root
        while p or len(l) > 0:
            if p:
                val += p.val
                l.append(p)
                p = p.left
            else:
                p = l.pop().right
        p = root
        while p or len(l) > 0:
            if p:
                l.append(p)
                p = p.left
            else:
                p = l.pop()
                p.val, val = val, val - p.val
                p = p.right
        return root
