class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num
        
        heapq.heapify(nums)
        for _ in range(k):
            curr = -heapq.heappop(nums)
        
        return curr