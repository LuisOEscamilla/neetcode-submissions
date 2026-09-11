class Solution:
    def trap(self, height: List[int]) -> int:
        leftMost = [0] * len(height)
        rightMost = [0] * len(height)

        leftMost[0] = height[0]
        for i in range(1, len(height)):
            leftMost[i] = max(leftMost[i-1], height[i])
        rightMost[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightMost[i] = max(rightMost[i+1], height[i])
        result = 0
        for i in range(len(height)):
            result += max(0,(min(leftMost[i],rightMost[i]) - height[i]))


        return result