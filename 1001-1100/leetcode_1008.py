class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        end = len(preorder)
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                end = i
                break
        p = TreeNode(preorder[0])
        p.left = self.bstFromPreorder(preorder[1:end])
        p.right = self.bstFromPreorder(preorder[end:])
        return p
