class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode):
        l = [root]
        while True:
            p = l[0]
            l = l[1:]
            if not p:
                for i in l:
                    if i:
                        return False
                return True
            else:
                l.append(p.left)
                l.append(p.right)
