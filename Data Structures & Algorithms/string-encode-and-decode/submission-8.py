class Solution:

    def encode(self, strs: List[str]) -> str:
        results = ""
        for s in strs:
            results += (str(len(s)) + '#' + s)
        return results



    def decode(self, s: str) -> List[str]:
        results = []
        ptr = 0
        while ptr < len(s):
            ptr2 = ptr
            while s[ptr2] != '#':
                ptr2 += 1
            currLen = int(s[ptr:ptr2])
            results.append(s[(ptr2+1):(ptr2+currLen+1)])
            ptr = ptr2 + currLen + 1

        return results