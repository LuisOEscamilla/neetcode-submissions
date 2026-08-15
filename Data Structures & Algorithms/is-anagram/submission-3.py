from collections import defaultdict
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)

        # return t == s
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for char in s:
            sDict[char] += 1
        for char in t:
            tDict[char] += 1

        return sDict == tDict