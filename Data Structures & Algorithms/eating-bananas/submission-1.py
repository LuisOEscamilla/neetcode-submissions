class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        currMin = end
        while start <= end:
            k = (start+end) // 2 #rate of eating bananas
            count = 0
            for i in range(len(piles)):
                count += piles[i] // k
                if piles[i] % k > 0:
                    count += 1
            if count <= h:
                currMin = min(currMin, k)
                end = k - 1
            else:
                start = k + 1
        
        return currMin
