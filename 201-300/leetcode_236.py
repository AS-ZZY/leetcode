class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNodetime(object):
    def __init__(self, x):
        self.node = x
        self.time = 1


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        l1 = []
        l2 = []
        x = TreeNodetime(root)
        l = [x]
        while x.node is not None or len(l) != 0:
            if x.node is None:
                x = l.pop()
                if x.time == 2:
                    x = TreeNodetime(None)
                else:
                    x.time += 1
                    l.append(x)
                    x = TreeNodetime(x.node.right)
            else:
                l.append(x)
                if x.node in [p, q]:
                    if len(l1) == 0:
                        l1 = l.copy()
                    else:
                        l2 = l.copy()
                        break
                x = TreeNodetime(x.node.left)
        for i in range(len(l2)):
            if l1[i].node.val != l2[i].node.val:
                return l1[i - 1].node.val
