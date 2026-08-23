class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = [0] * len(nums)
        prev = 0
        prevPrev = 0
        for i in range(len(nums)):
            if nums[i] + prevPrev >= prev:
                maxMoney[i] = nums[i] + prevPrev
            else:
                maxMoney[i] = prev
            prevPrev = prev
            prev = maxMoney[i]

        return maxMoney[-1]