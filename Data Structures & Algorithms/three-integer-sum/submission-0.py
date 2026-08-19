class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #two sum implementation
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + val > 0:
                    r -= 1
                elif nums[l] + nums[r] + val < 0:
                    l += 1
                else:
                    results.append([nums[l], nums[r], val])
                    l += 1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1



        return results
    #     results = []
    #     used = set()
    #     for i in range(len(nums)):
    #         if nums[i] not in used:
    #             target = -nums[i]
    #             twoSumVal = self.twoSum(nums[i+1:], target)
    #             for vals in twoSumVal:
    #                 results.append([target, vals[0], vals[1]])
    #             used.add(nums[i])
        
    #     return results

    # #implement two sum    
    # def twoSum(self, nums, target):
    #     numSet = set()
    #     results = []
    #     used = set()
    #     for num in nums:
    #         if (target - num) in numSet and num not in used:
    #             results.append([num, (target-num)])
    #             used.add(num)
    #         numSet.add(num)
    #     return results