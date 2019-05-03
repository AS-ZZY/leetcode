class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.node = root
        self.x = 0


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        l = []
        lval = []
        p = Tree(root)
        while p.node is not None or len(l) != 0:
            if p.node is not None:
                l.append(p)
                p = Tree(p.node.left)
            else:
                p = l.pop()
                if p.x == 0:
                    p.x = 1
                    l.append(p)
                    p = Tree(p.node.right)
                else:
                    lval.append(p.node.val)
                    p = Tree(None)
        return lval