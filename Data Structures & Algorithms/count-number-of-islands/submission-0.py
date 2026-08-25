from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        stack = deque()
        totalIslands = 0
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    stack.append((i,j))
                    totalIslands += 1
                    visited.add((i,j))
                    while stack:
                        y,x = stack.pop()
                        neighbors = self.findNeighbors(grid,y,x)
                        for neighbor in neighbors:
                            if neighbor not in visited:
                                stack.append(neighbor)
                                visited.add(neighbor)


        return totalIslands





    def findNeighbors(self, grid, y, x):
        neighbors = set()
        if x > 0 and grid[y][x-1] == "1":
            neighbors.add((y,x-1))
        if x < len(grid[0]) - 1 and grid[y][x+1] == "1":
            neighbors.add((y,x+1))
        if y > 0 and grid[y-1][x] == "1":
            neighbors.add((y-1,x))
        if y < len(grid) - 1 and grid[y+1][x] == "1":
            neighbors.add((y+1,x))

        return neighbors