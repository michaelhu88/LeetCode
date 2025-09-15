"""
row * col == total number of items

total // 2 is mid point
mid // 4
mid % 4

"""



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // COLS
            col = mid % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False