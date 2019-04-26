class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        nodes = [root]
        re = []
        while True:
            vals, nodes = self.walk(nodes)
            re.append(vals)
            if len(nodes) == 0:
                break
        re.reverse(inplace = True)
        return re


    def walk(self, l):
        nodes = []
        vals = []
        for i in l:
            vals.append(i.val)
            if i.left is not None:
                nodes.append(i.left)
            if i.right is not None:
                nodes.append(i.right)
        return vals, nodes
