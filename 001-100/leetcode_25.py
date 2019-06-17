class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        x = ListNode(0)
        x.next = head
        self.start(x, k)
        p = x.next
        del x
        return p
    
    def start(self, x, k):
        j = x.next
        num = 1
        while j is not None and num < k:
            j = j.next
            num += 1
        if j is None:
            return 
        num = 2
        j = x.next 
        while num <= k:
            num += 1
            p = j.next
            j.next = p.next
            p.next = x.next
            x.next = p
        self.start(j, k)

