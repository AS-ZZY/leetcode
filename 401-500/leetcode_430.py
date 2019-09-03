class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node'):

        def change(a):
            while a is not None and (a.child is not None or a.next is not None):
                if a.child is not None:
                    b = a.next
                    a.next = a.child
                    a.child = None
                    a.next.prev = a
                    c = change(a.next)
                    if b is not None:
                        c.next = b
                        b.prev = c
                    a = b
                else:
                    a = a.next
            return a
        
        change(head)
        return head
