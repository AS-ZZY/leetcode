class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode):
        if head is None or head.next is None or head.next.next is None:
            return 
        a = head
        b = head
        while a.next is not None and a.next.next is not None:
            a = a.next.next
            b = b.next
        a = b.next
        while a.next is not None:
            c = a.next
            a.next = a.next.next
            c.next = b.next
            b.next = c
        a = head
        while a != b:
            c = b.next
            b.next = b.next.next
            c.next = a.next
            a.next = c
            a = a.next.next



