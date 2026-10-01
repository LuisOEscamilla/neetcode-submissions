class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def helper(string, o, c):
            if o == n and c == n:
                results.append(string)
                return
            if o < n:
                helper(string + "(", o+1, c)
            if c < o and c < n:
                helper(string + ")", o, c+1)

        helper("", 0, 0)
        return results