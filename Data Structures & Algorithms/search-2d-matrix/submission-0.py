class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        row = -1 
        while start <= end:
            mid = (start+end) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                end = mid - 1
        
        if row == -1:
            return False
        
        start, end = 0, len(matrix[0]) - 1
        while start <= end:
            mid = (start+end) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False