class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sums: int):
        if not root:
            return []
        result = []

        def getList(l, r, s):
            l.append(r.val)
            if not r.left and not r.right:
                if s + r.val == sums:
                    l1 = l.copy()
                    result.append(l1)
                    return
            if r.left:
                l1 = l.copy()
                getList(l1, r.left, s + r.val)
            if r.right:
                l1 = l.copy()
                getList(l1, r.right, s + r.val)

        getList([], root, 0)
        return result
