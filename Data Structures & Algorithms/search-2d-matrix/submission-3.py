class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: 找最后一个起始值 <= target 的行
        top, bottom = 0, m
        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target:
                top = mid + 1
            else:
                bottom = mid
        
        row = top - 1  # 最后一行 ≤ target 的起始值
        if row < 0: return False  # target 比第一行还小

        # Step 2: 在该行中二分查找
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True

        return False