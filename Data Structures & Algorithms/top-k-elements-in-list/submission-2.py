from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary = defaultdict(int)
        # for num in nums:
        #     dictionary[num] += 1
        # results = []
        
        # while k > 0:
        #     currMax = max(dictionary, key=dictionary.get)
        #     k -= 1
        #     results.append(currMax)
        #     dictionary.pop(currMax)


        # return results
        myDict = defaultdict(int)
        for n in nums:
            myDict[n] += 1

        count = [[] for i in range(len(nums) + 1)]
        results = []
        for key, val in myDict.items():
            count[val].append(key)


        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                results.append(num)
                if len(results) == k:
                    return results
        