class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        def helper(curr, i, total):
            if total == target:
                results.append(curr[:])
                return

            if i == len(candidates) or total > target:
                return

            curr.append(candidates[i])
            helper(curr, i + 1, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            helper(curr, i + 1, total)



        helper([], 0, 0)
        return results
