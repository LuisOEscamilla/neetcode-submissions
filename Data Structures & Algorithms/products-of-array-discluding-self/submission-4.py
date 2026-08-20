class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        currProd = 1
        #Left most product
        for i in range(1, len(nums)):
            currProd *= nums[i-1]
            output[i] = currProd
        #right most product
        currProd = 1
        for i in range(len(nums) - 2, -1, -1):
            currProd *= nums[i+1]
            output[i] *= currProd
        return output
        