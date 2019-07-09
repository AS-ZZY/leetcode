class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        l = []
        a = {}
        max1 = 1
        p = root
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                if p.val in a.keys():
                    a[p.val] += 1
                    if max1 < a[p.val]:
                        max1 = a[p.val]
                else:
                    a[p.val] = 1
                p = p.right
            else:
                l.append(p)
                p = p.left
        re = []
        for i in a.keys():
            if a[i] == max1:
                re.append(i)
        return re
