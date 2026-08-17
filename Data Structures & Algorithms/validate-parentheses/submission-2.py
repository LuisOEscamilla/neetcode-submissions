from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if c == ')':
                    if top != '(':
                        return False
                elif c == ']':
                    if top != '[':
                        return False
                elif c == '}':
                    if top != '{':
                        return False
                else:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else: 
            return False