class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        p = l1
        q = l2
        k = ListNode(0)
        k.next = None
        o = k
        while p is not None and q is not None:
            c = p.val + q.val + a
            if c >= 10:
                c -= 10
                a = 1
            else:
                a = 0
            pp = ListNode(c)
            pp.next = o.next
            o.next = pp
            o = o.next
            p = p.next
            q = q.next
        while p is not None:
            c = p.val + a
            if c >= 10:
                c -= 10
                a = 1
            else:
                a = 0
            pp = ListNode(c)
            pp.next = o.next
            o.next = pp
            o = o.next
            p = p.next
        while q is not None:
            c = q.val + a
            if c >= 10:
                c -= 10
                a = 1
            else:
                a = 0
            pp = ListNode(c)
            pp.next = o.next
            o.next = pp
            o = o.next
            q = q.next
        if a == 1:
            pp = ListNode(1)
            pp.next = o.next
            o.next = pp
        return k.next
