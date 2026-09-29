class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i, num in enumerate(nums):
            heapq.heappush(maxHeap, num)
            if i >= k:
                heapq.heappop(maxHeap)
        
        curr = heapq.heappop(maxHeap)
        return curr