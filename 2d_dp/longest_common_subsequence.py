class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for row in range(len(text1)-1, -1, -1):
            for col in range(len(text2)-1, -1, -1):
                if text1[row] == text2[col]:
                    arr[row][col] = 1 + arr[row+1][col+1]
                else:
                    arr[row][col] = max(arr[row+1][col], arr[row][col+1])
        
        return arr[0][0]
