class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,visited,remainingWord):
            if not remainingWord:
                return True
            if 0 > r or r >= len(board):
                return False
            if 0 > c or c >= len(board[0]):
                return False
            if board[r][c] != remainingWord[0] or (r,c) in visited:
                return False
            visited.add((r,c))
            found = dfs(r+1,c,visited,remainingWord[1:]) or dfs(r-1,c,visited,remainingWord[1:]) or dfs(r,c+1,visited,remainingWord[1:]) or dfs(r,c-1,visited,remainingWord[1:])
            visited.remove((r,c))
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c,set(),word):
                        return True

        

        return False