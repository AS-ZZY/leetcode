from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        dic = defaultdict(lambda: -1)
        start = 0
        maxlen = -1
        for i in range(len(s)):
            if dic[s[i]] < start:
                dic[s[i]] = i
            else:
                end = i
                if maxlen < end - start:
                    maxlen = end - start
                start = dic[s[i]] + 1
                dic[s[i]] = i
        if maxlen < len(s) - start:
            maxlen = len(s) - start
        return maxlen
