class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode):
        if root is None:
            return 0
        num = ""
        l = []
        self.getnum(num, root, l)
        m = 0
        for i in l:
            m += int(i)
        return m
        
        

    def getnum(self, num, root, l):
        if root is None:
            return
        p = num + str(root.val)
        if root.right is None and root.left is None:
            l.append(p)
        else:
            self.getnum(p, root.left, l)
            self.getnum(p, root.right, l)