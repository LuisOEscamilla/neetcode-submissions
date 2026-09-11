from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = defaultdict(int)
        for c in s1:
            count[c] += 1
        seen = defaultdict(int)
        end = 0
        while end < len(s1):
            seen[s2[end]] += 1
            end += 1
        if seen == count:
            return True
        start = 0
        while end < len(s2):
            seen[s2[start]] -= 1
            if seen[s2[start]] == 0:
                del seen[s2[start]]
            seen[s2[end]] += 1
            if seen == count:
                return True
            start += 1
            end += 1
            


        return False