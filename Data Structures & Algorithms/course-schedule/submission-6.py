class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        d = {}
        for i in range(numCourses):
            d[i] = []
        for c, p in prerequisites:
            d[c].append(p)
        def dfs(course): 
            if course in visited:
                return False    
            if d[course] == []:
                return True
            visited.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False
                
            visited.remove(course)
            d[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True