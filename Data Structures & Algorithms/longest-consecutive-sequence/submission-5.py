class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numsSet = set()

        for num in nums:
            numsSet.add(num)
        maxCount = 0
        for num in nums:
            currCount = 0
            i = 0  
            if num - 1 not in numsSet:
                while num+i in numsSet:
                    currCount += 1
                    i += 1
                maxCount = max(maxCount, currCount)
        return maxCount