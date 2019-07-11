class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        if root is None:
            return None
        l = [root]
        while True:
            ll = []
            for i in l:
                if i.left is not None:
                    ll.append(i.left)
                if i.right is not None:
                    ll.append(i.right)
            if len(ll) == 0:
                break
            l = ll
        return l[0]


