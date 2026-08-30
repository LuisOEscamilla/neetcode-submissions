class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def helper(curr, i):
            if i >= len(nums) or sum(curr) > target:
                return
            if sum(curr) == target:
                results.append(curr)
                return
            helper(curr + [nums[i]], i)
            helper(curr, i+1)


        helper([], 0)
        return results
