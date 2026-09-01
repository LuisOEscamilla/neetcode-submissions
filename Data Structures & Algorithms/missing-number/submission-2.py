class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = ((len(nums)+1)*(len(nums))) // 2
        currSum = sum(nums)
        if totalSum == currSum:
            return 0
        else:
            return totalSum-currSum