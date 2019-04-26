 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


 class Solution:
     def levelOrder(self, root: TreeNode) -> List[List[int]]:
         if root is None:
             return []
         l = [root]
         re = []
         c = [root.val]
         while len(l) != 0:
             re.append(c)
             c, l = self.walk(l)
         return re

     def walk(self, l):
         t = []
         ll = []
         for i in l:
             if i.left is not None:
                 t.append(i.left.val)
                 ll.append(i.left)
             if i.right is not None:
                 t.append(i.right.val)
                 ll.append(i.right)
         return t, ll