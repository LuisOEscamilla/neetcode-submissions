class Solution:
    def isPalindrome(self, s: str) -> bool:       
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not self.isValid(s[start]):
                start += 1
            while start < end and not self.isValid(s[end]):
                end -= 1
            
            if (s[start].lower() != s[end].lower()):
                return False
            start += 1
            end -= 1
        return True

    def isValid(self, char):
        if char.isalpha() or char.isdigit():
            return True
        return False