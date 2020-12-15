class Solution:
    def lowestCommonAncestor(self, root, m1, m2):
        if not root:
            return None
        p, q = min([m1.val, m2.val]), max([m1.val, m2.val])
        x = root
        while True:
            if p <= x.val and q >= x.val:
                return x
            elif x.val < p:
                x = x.right
            else:
                x = x.left
