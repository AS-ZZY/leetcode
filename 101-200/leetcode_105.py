class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if len(preorder) == 0:
            return None
        a = preorder[0]
        root = TreeNode(a)
        b = inorder.index(a)
        root.left = self.buildTree(preorder[1 : b + 1], inorder[0 : b])
        root.right = self.buildTree(preorder[b + 1 :], inorder[b + 1:])
        return root

