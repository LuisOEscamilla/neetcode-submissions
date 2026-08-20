from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        tDict = defaultdict(int)
        for char in t:
            tDict[char] += 1
        have, need = 0, len(tDict)
        start = 0
        sDict = defaultdict(int)
        for i in range(len(s)):
            sDict[s[i]] += 1
            if s[i] in tDict and sDict[s[i]] == tDict[s[i]]:
                have += 1
            while have == need:
                if result == "":
                    result = s[start:i+1]
                elif(i - start) < len(result):
                    result = s[start:i+1]
                
                sDict[s[start]] -= 1
                if s[start] in tDict and sDict[s[start]] < tDict[s[start]]:
                    have -= 1
                start += 1

        return result

