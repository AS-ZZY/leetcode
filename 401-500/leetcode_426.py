class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        l = [root]
        re = [[root.val]]
        while len(l) != 0:
            ll = []
            vals = []
            for i in l:
                for j in i.children:
                    ll.append(j)
                    vals.append(j.val)
            l = ll
            if len(vals) != 0:
                re.append(vals)
        return re