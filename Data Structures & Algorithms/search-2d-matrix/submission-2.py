class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols

        left = 0
        right = total - 1

        while left <= right:
            midpoint = (left + right) // 2

            # TODO: Need to understand why i/j is equal to this
            i = midpoint // cols
            j = midpoint % cols

            if matrix[i][j] == target:
                return True

            elif matrix[i][j] < target:
                left = midpoint + 1

            else:
                right = midpoint - 1

        return False
        