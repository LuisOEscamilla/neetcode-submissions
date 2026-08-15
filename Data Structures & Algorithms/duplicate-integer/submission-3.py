class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False