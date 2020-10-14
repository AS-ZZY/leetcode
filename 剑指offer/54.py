class Solution:
    def kthLargest(self, root, k: int):
        l = []
        values = []
        p = root
        while p is not None or len(l) != 0:
            if p is None:
                p = l[-1]
                values.append(p.val)
                p = p.right
                l = l[:-1]
            else:
                l.append(p)
                p = p.left
        return values[-k]