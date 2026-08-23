class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prevPrev = 0
        for i in range(len(nums)):
            temp = max(nums[i]+prevPrev, prev)
            prevPrev = prev
            prev = temp

        return prev