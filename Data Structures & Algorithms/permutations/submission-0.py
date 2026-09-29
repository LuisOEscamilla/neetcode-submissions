class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def helper(curr, left, i):
            if not left and curr:
                results.append(curr[:])
            if i == len(left):
                return 
            
            curr.append(left[i])
            helper(curr, left[:i]+left[i+1:], 0)
            curr.pop()
            helper(curr, left, i+1)
                

        helper([], nums[:], 0)

        return results