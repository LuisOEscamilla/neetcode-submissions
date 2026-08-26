from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestWord = ""
        longestCount = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > longestCount:
                    longestWord = s[l:r+1]
                    longestCount = (r-l + 1)
                l -= 1
                r += 1

        for i in range(len(s) - 1):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > longestCount:
                    longestWord = s[l:r+1]
                    longestCount = (r-l + 1)
                l -= 1
                r += 1


        return longestWord