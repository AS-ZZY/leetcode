import functools


class Solution:
    @functools.lru_cache(None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False

        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3

        res1 = False
        res2 = False
        if s1[0] == s3[0]:
            res1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            res2 = self.isInterleave(s1, s2[1:], s3[1:])

        return res1 or res2
