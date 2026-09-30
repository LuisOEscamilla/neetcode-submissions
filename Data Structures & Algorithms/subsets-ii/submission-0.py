class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def helper(curr, i):
            if i >= len(nums):
                results.append(curr[:])
                return 
            curr.append(nums[i])
            helper(curr, i+1)
            curr.pop()
            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(curr, i+1)

        helper([], 0)
        return results

        