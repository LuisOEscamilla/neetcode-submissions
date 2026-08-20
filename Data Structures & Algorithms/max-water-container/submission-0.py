class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1

        maxVol = 0  
        while start < end:
            currVol = min(heights[start], heights[end]) * (end-start)   
            maxVol = max(maxVol, currVol)
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return maxVol