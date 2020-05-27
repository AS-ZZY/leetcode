class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head
        q = p.next
        dic = {}
        dic[0] = p
        a = 0
        while q:
            a += q.val
            if a in dic.keys():
                s = dic[a].next
                d = a
                while s != q.next:
                    d += s.val
                    try:
                        if dic[d] is s:
                            del dic[d]
                    except:
                        pass
                    s = s.next
                dic[a].next = q.next
            else:
                dic[a] = q
            q = q.next
        return p.next