class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        currMin = nums[start]
        while start <= end:
            if nums[start] < nums[end]:
                currMin = min(currMin, nums[start])
                break
            mid = (start+end) // 2
            currMin = min(currMin, nums[mid])
            if nums[mid] >= nums[start]: #right sorted
                start = mid + 1
            else: #nums[mid] > nums[start] left sorted
                end = mid - 1

        return currMin