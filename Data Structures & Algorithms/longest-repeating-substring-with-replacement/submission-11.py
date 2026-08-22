from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        count = defaultdict(int)
        longestLen = 0
        for end in range(len(s)):
            count[s[end]] += 1
            if (end-start + 1) - max(count.values()) > k:
                count[s[start]] -= 1
                start += 1
            longestLen = max(longestLen, (end-start + 1))
            



        return longestLen