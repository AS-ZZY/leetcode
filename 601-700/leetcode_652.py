class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        res = []
        lookup = defaultdict(int)

        def helper(root):
            if not root:
                return "#"
            s = helper(root.left) + "," + \
                helper(root.right) + "," + str(root.val)
            if lookup[s] == 1:
                res.append(root)
            lookup[s] += 1
            return s
        helper(root)
        return res
