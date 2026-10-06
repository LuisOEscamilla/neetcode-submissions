class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        d = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y", "z"]}

        def helper(curr, i):
            if i == len(digits):
                results.append(curr[:])
                return
            for char in d[digits[i]]:
                helper(curr + char, i+1)
            
        if digits:
            helper("", 0)    

        return results