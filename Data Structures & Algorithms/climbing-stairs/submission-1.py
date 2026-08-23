class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(curr, n, array):
            if curr < 0:
                return array
            if curr == n:
                array[curr] = 1

            elif curr == n - 1:
                array[curr] = array[curr+1]
            else:
                array[curr] = array[curr+1] + array[curr+2]
            array = helper(curr-1, n, array)
            return array
        array = [0] * (n+1)
        results = helper(n, n, array)
        return results[0]