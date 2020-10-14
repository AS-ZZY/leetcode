class Solution:
    def canVisitAllRooms(self, rooms):
        s1 = set()
        s2 = [0]

        while len(s2) > 0:
            i = s2[0]
            s2 = s2[1:]
            if i in s1:
                pass
            else:
                s1.add(i)
                s2 = list(set(s2 + rooms[i]))
        
        if len(s1) == len(rooms):
            return True
        return False