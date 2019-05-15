class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        re = [root.val]
        if len(root.children) == 0:
            return re
        l = [[root, 0]]
        while len(l) != 0:
            q = l.pop()
            p = q[0].children[q[1]]
            re.append(p.val)
            if q[1] + 1 < len(q[0].children):
                l.append([q[0], q[1] + 1])
            if len(p.children) != 0:
                l.append([p, 0])
        return re