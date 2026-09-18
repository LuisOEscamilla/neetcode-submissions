class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                temp, day = stack[-1]
                results[i] = day - i
            else:
                results[i] = 0
            stack.append((temperatures[i], i))

        return results