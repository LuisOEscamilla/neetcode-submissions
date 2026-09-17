class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append((val1+val2))
            elif t == "-":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append((val1-val2))

            elif t == "*":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append((val1*val2))
            elif t == '/':
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(int(val1/val2))
            else:
                stack.append(int(t))
        return stack[-1]