class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxSub = 0
        start, end = 0,0
        seen = set()

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                maxSub = max(maxSub, end-start)
            else:
                while s[start] != s[end]:
                    seen.discard(s[start])
                    start += 1
                seen.discard(s[start])
                start += 1
                
        return maxSub

# (b,c,d,b,e,f)