class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode):
        p = ListNode(0)
        p.next = None
        q = head
        while q is not None:
            s = q.next
            q.next = p.next
            p.next = q
            q = s
        return p.next