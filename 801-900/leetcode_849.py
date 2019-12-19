class Solution(object):
    def maxDistToClosest(self, seats):
        str_seats = ''.join(str(x) for x in seats)
        empty = str_seats.split('1')
        max_empty = max(len(x) for x in empty)
        return max((max_empty+1)//2, len(empty[0]), len(empty[-1])) 