class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        p = TreeNode(val)
        p.left = root
        return p
