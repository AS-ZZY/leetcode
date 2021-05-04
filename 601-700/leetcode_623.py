class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int):
        if depth == 1 or not root:
            p = TreeNode(val)
            p.left = root
            return p
        deep = 1
        l = [root]
        while deep < depth - 1:
            deep += 1
            ll = []
            for i in l:
                if i.left:
                    ll.append(i.left)
                if i.right:
                    ll.append(i.right)
            l = ll
            if len(l) == 0:
                p = TreeNode(val)
                p.left = root
                return p
        for i in l:
            p = TreeNode(val)
            p.left = i.left
            i.left = p
            p = TreeNode(val)
            p.right = i.right
            i.right = p
        return root
