class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = currArea = 0
        visited = set()
        stack = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    stack.append((row,col))
                    visited.add((row,col))
                    currArea = 0
                while stack:
                    x, y = stack.pop()
                    currArea += 1
                    neighbors = []
                    for d in directions:
                        if 0 <= x+d[0] < len(grid) and 0 <= y+d[1] < len(grid[0]) and grid[x+d[0]][y+d[1]] == 1:
                            neighbors.append((x+d[0],y+d[1]))
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)
                maxArea = max(currArea, maxArea)


        return maxArea