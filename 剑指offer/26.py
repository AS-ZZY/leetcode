class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        
        def start(a, b):
            if b is None:
                return True
            if a is None:
                return False
            if a.val != b.val:
                return False
            return start(a.left, b.left) and start(a.right, b.right)

        if B is None or A is None:
            return False
        
        return start(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)