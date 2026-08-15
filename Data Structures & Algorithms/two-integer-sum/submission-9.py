class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start = 0
        # end = len(nums) - 1
        # while start < end:
        #     if nums[start] + nums[end] == target:
        #         return [start, end]
        #     elif nums[start] + nums[end] < target:
        #         start += 1
        #     elif nums[start] + nums[end] > target:
        #         end -= 1

        hashMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i
        return None

        