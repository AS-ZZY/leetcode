class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> int:
        self.re = 0
        self.pathList(root, 0, {0: 1}, sums)
        return self.re
        
    def pathList(self, root, s, d, sums):
        if root is None:
            return
        
        dic = d.copy()
        s = s + root.val
        try:
            self.re += dic[s - sums]
        except:
            pass
            
        try:
            dic[s] += 1
        except:
            dic[s] = 1
    
        self.pathList(root.left, s, dic, sums)
        self.pathList(root.right, s, dic, sums)