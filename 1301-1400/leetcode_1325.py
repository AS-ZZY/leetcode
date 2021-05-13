class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, node):
        self.node = node
        self.num = 1


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int):
        root2 = Tree(root)
        l = []
        p = root2
        none = Tree(None)
        while len(l) != 0 or p.node:
            if p.node:
                l.append(p)
                p = Tree(p.node.left)
            else:
                p = l.pop()
                if p.num == 1:
                    p.num = 2
                    l.append(p)
                    p = Tree(p.node.right)
                else:
                    if not p.node.left and not p.node.right and p.node.val == target:
                        if len(l) > 0:
                            if l[-1].num == 1:
                                l[-1].node.left = None
                            else:
                                l[-1].node.right = None
                        else:
                            return None
                    p = none
        return root
