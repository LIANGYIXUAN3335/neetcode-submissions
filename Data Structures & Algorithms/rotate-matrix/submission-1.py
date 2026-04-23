class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left , right = 0, n-1
        while left < right:
            for i in range(right - left):
                temp = matrix[left][left + i]
                matrix[left][left + i] = matrix[right - i][left]
                matrix[right - i][left] = matrix[right][right - i]
                matrix[right][right - i] = matrix[left + i][right]
                matrix[left + i][right] = temp
            left += 1
            right -= 1
        



        