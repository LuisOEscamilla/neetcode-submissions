from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def findN(r,c):
            n = []
            if r > 0 and heights[r][c] <= heights[r-1][c]:
                n.append((r-1,c))
            if r < len(heights) - 1 and heights[r][c] <= heights[r+1][c]:
                n.append((r+1,c))
            if c > 0 and heights[r][c] <= heights[r][c-1]:
                n.append((r,c-1))
            if c < len(heights[0]) - 1 and heights[r][c] <= heights[r][c+1]:
                n.append((r,c+1))
            return n
        pacific = set()
        atlantic = set()

        #pacific dfs
        stack = deque()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    stack.append((r,c))
                    pacific.add((r,c))
                    while stack:
                        row,col = stack.pop()
                        for n in findN(row,col):
                            if n not in pacific:
                                stack.append((n))
                                pacific.add(n)

        #atla dfs
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == len(heights)-1 or c == len(heights[0])-1:
                    stack.append((r,c))
                    atlantic.add((r,c))
                    while stack:
                        row,col = stack.pop()
                        for n in findN(row,col):
                            if n not in atlantic:
                                stack.append((n))
                                atlantic.add(n)


        results = []
        for coord in pacific:
            if coord in atlantic:
                results.append(list(coord))
        return results