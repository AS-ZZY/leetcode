class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        
        def getList(l, time):
            re = []
            l2 = []
            while len(l) > 0:
                p = l[0]
                re.append(p.val)
                if p.left:
                    l2.append(p.left)
                if p.right:
                    l2.append(p.right)
                l = l[1:]
            if time % 2 == 0:
                re = re[::-1]
            result.append(re)
            if len(l2) > 0:
                getList(l2, time + 1)
        
        if root is None:
            return []
        result = []
        l = [root]
        getList(l, 1)
        return result