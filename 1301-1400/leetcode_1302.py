class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode):
        if not root:
            return 0
        l = [root]
        while True:
            s = 0
            ll = []
            for i in l:
                s += i.val
                if i.left:
                    ll.append(i.left)
                if i.right:
                    ll.append(i.right)
            l = ll
            if len(l) == 0:
                return s
