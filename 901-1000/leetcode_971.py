class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage):
        if not root:
            return [-1] if len(voyage) > 0 else []
        if len(voyage) == 0 or root.val != voyage[0]:
            return [-1]
        re = []
        if not root.left or not root.right:
            q = root.left if root.left else root.right
            re = self.flipMatchVoyage(q, voyage[1:])
        else:
            if root.left.val != voyage[1]:
                root.left, root.right = root.right, root.left
                re = [root.val]
            try:
                index = voyage.index(root.right.val)
                left = self.flipMatchVoyage(root.left, voyage[1:index])
                right = self.flipMatchVoyage(root.right, voyage[index:])
                if (len(left) > 0 and left[0] == -1) or (len(right) > 0 and right[0] == -1):
                    re = [-1]
                else:
                    re.extend(left + right)
            except:
                re = [-1]
        return re
