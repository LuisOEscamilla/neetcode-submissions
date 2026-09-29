class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        def helper(curr, i):
            if i == len(nums):
                return
        
            curr.append(nums[i])
            results.append(curr[:])
            helper(curr, i+1)
            curr.pop()
            helper(curr, i+1)

        helper([], 0)
        return results