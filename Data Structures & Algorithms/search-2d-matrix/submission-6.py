class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) 
        while top < bottom :
            mid = (bottom - top) // 2 + top
            if matrix[mid][0] > target:
                bottom = mid 
            else:
                top = mid + 1
        left, right = 0, len(matrix[0]) -1
        row = top - 1
        if row < 0:
            return False
        while left <= right:
            mid = (right - left) // 2 + left
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False
        