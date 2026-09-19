class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPos = []
        stack = []
        for i, val in enumerate(position):
            sortedPos.append((val, i))
        sortedPos.sort()
        for val, i in reversed(sortedPos):
            if stack:
                totalTime = (target - val) / speed[i]
                if totalTime > stack[-1]:
                    stack.append(totalTime) 
                
            else:
                totalTime = (target - val) / speed[i]
                stack.append(totalTime) 
        return len(stack)
       

        
    