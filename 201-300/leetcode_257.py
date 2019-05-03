class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        global re
        re = []
        s = ""
        self.fun(root, s)
        return re

    def fun(self, root, s):
        if root is None:
            return
        if s != "":
            s = s + "->" + str(root.val)
        else:
            s = str(root.val)
        if root.left is None and root.right is None:
            re.append(s)
            return
        if root.left is not None:
            self.fun(root.left, s)
        if root.right is not None:
            self.fun(root.right, s)




