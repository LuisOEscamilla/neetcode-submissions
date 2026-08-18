from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        count = 0
        for word in strs:
            anagrams["".join(sorted(word))].append(count)
            count += 1

        results = []
        for key in anagrams.keys():
            subList = []
            for val in anagrams[key]:
                subList.append(strs[val])
            results.append(subList)
        return results