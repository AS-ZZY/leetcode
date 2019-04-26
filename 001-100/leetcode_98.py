 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        l = []
        p = root
        f = False
        a = 0
        while p is not None or len(l) != 0:
            if p is None:
                p = l.pop()
                if not f:
                    f = True
                    a = p.val
                else:
                    if a >= p.val:
                        return False
                    else:
                        a = p.val
                p = p.right
            else:
                l.append(p)
                p = p.left
        return True
