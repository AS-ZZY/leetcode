class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode):
        head = TreeNode(0)
        q = head
        l = []
        p = root
        while p or len(l) > 0:
            if not p:
                p = l.pop()
                q.right = p
                q = q.right
                p = p.right
            else:
                l.append(p)
                p = p.left
        q = head.right
        del head
        return q
