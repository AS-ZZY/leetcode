class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode):
        
        def isSubtree2(s, t):
            if s is None and t is None:
                return True
            elif s is None or t is None:
                return False
            if s.val == t.val:
                return isSubtree2(s.left, t.left) and isSubtree2(s.right, t.right)
            else:
                return False
        
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        a = False
        if s.val == t.val:
            a = isSubtree2(s.left, t.left) and isSubtree2(s.right, t.right)
        return a or self.isSubtree(s.left, t) or self.isSubtree(s.right, t) 
