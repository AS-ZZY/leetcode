class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        if not root:
            return

        def getNode(r, v, l):
            if not r:
                return []
            if r.level - l == v:
                return [r.val]
            return getNode(r.left, v, l) + getNode(r.right, v, l)

        root.times, root.level = 1, 0
        l, p, ll = [root], root.left, []
        s, ss = [], []
        while p or len(l):
            if not p:
                p = l.pop()
            else:
                try:
                    p.times
                except:
                    p.times = 0
                if p.times == 0:
                    p.times = 1
                    p.level = l[-1].level + 1
                    l.append(p)
                    p = p.left
                elif p.times == 1:
                    p.times = 2
                    l.append(p)
                    p = p.right
                else:
                    s.append(p.val)
                    ss.append(p.level)
                    if p == target:
                        ll = l.copy()
                        ll.append(p)
                    p = None
        level, re = ll[-1].level, []
        for ii in range(len(ll) - 1):
            i = ll[ii]
            if level - i.level > k:
                pass
            elif level - i.level == k:
                re.append(i.val)
            else:
                a = i.left if i.left != ll[ii + 1] else i.right
                re = re + getNode(a, k - (level - i.level), i.level)
        p, l = ll[-1], []
        while p or len(l):
            if not p:
                p = l.pop().right
            else:
                l.append(p)
                if p.level - level == k:
                    re.append(p.val)
                p = p.left
        return re
