class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        p, q = l1, l2
        m, n = 0, 0
        while p:
            p = p.next
            m += 1
        while q:
            q = q.next
            n += 1
        if m > n:
            p, q = l1, l2
        else:
            p, q = l2, l1
        start = ListNode(0)
        start.next = ListNode(0)
        j = start
        for _ in range(1, abs(m - n) + 1):
            newNode = ListNode(p.val)
            p = p.next
            j = start.next
            start.next = newNode
            newNode.next = j
        while p:
            newNode = ListNode(p.val + q.val)
            p = p.next
            q = q.next
            j = start.next
            start.next = newNode
            newNode.next = j
        j = start.next
        while j:
            if j.val >= 10:
                j.val -= 10
                j.next.val += 1
            j = j.next
        j = start.next
        start.next = None
        while j:
            k = j.next
            j.next = start.next
            start.next = j
            j = k
        if start.next.val != 0:
            return start.next
        return start.next.next
