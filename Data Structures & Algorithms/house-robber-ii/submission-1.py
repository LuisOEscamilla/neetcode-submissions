class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prevPrev = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) -1):
            temp = max(prevPrev+nums[i], prev)
            prevPrev = prev
            prev = temp

        max1 = prev

        prev = 0
        prevPrev = 0
        for i in range(1, len(nums)):
            temp = max(prevPrev+nums[i], prev)
            prevPrev = prev
            prev = temp
        max2 = prev
        return max(max1, max2)