# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        n = 0
        l1 = [root]
        while len(l1) > 0:
            l2 = []
            for i in l1:
                if i.left:
                    if i.left.val in [x, y]:
                        if n == 1:
                            return True
                        if i.right and i.right.val in [x, y]:
                            return False
                        else:
                            n += 1
                    l2.append(i.left)
                if i.right:
                    if i.right.val in [x, y]:
                        if n == 1:
                            return True
                        n += 1
                    l2.append(i.right)
            if n == 1:
                return False
            l1 = l2