from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1
        results = []
        
        while k > 0:
            currMax = max(dictionary, key=dictionary.get)
            k -= 1
            results.append(currMax)
            dictionary.pop(currMax)


        return results