class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 1
        while i * i <= n:
            i += 1
        return i

            
            