class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        curr = []

        def helper(o, c):
            if o == n and c == n:
                results.append("".join(curr))
                return

            if o < n:
                curr.append("(")
                helper(o + 1, c)
                curr.pop()

            if c < o:
                curr.append(")")
                helper(o, c + 1)
                curr.pop()

        helper(0, 0)
        return results