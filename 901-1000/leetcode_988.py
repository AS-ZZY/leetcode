class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree():
    def __init__(self, node):
        self.node = node
        self.num = 1


class Solution:
    def smallestFromLeaf(self, root: TreeNode):
        l = []
        head = Tree(root)
        p = head
        re = ""
        while len(l) > 0 or p.node:
            if not p.node:
                p = l.pop()
                if p.num == 2:
                    p = Tree(None)
                else:
                    p.num = 2
                    l.append(p)
                    p = Tree(p.node.right)
            else:
                if not p.node.left and not p.node.right:
                    s = ""
                    for i in l:
                        s = chr(i.node.val + ord("a")) + s
                    s = chr(p.node.val + ord("a")) + s
                    if not re or re > s:
                        re = s
                l.append(p)
                p = Tree(p.node.left)
        return re
