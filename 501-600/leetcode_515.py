class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        re = []
        l = [root]
        while len(l) != 0:
            ll = []
            maxV = float("-inf")
            for i in l:
                if maxV < i.val:
                    maxV = i.val
                if i.left:
                    ll.append(i.left)
                if i.right:
                    ll.append(i.right)
            l = ll
            re.append(maxV)
        return re
