"""
one dictionary for rows (9 in total)
index : set

one dictionary for cols (9 in total)
index: set

one dictionary for boxes (9 in total)
index: set

for row in range



"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmRow = defaultdict(set)
        hmCol = defaultdict(set)
        hmBox = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] not in hmRow[row]:
                        hmRow[row].add(board[row][col])
                    else:
                        return False
                    if board[row][col] not in hmCol[col]:
                        hmCol[col].add(board[row][col])
                    else:
                        return False
                    
                    if 0 <= row <= 2 and 0 <= col <= 2:
                        if board[row][col] not in hmBox[0]:
                            hmBox[0].add(board[row][col])
                        else:
                            return False
                    
                    if 0 <= row <= 2 and 3 <= col <= 5:
                        if board[row][col] not in hmBox[1]:
                            hmBox[1].add(board[row][col])
                        else:
                            return False

                    if 0 <= row <= 2 and 6 <= col <= 8:
                        if board[row][col] not in hmBox[2]:
                            hmBox[2].add(board[row][col])
                        else:
                            return False

                    if 3 <= row <= 5 and 0 <= col <= 2:
                        if board[row][col] not in hmBox[3]:
                            hmBox[3].add(board[row][col])
                        else:
                            return False

                    if 3 <= row <= 5 and 3 <= col <= 5:
                        if board[row][col] not in hmBox[4]:
                            hmBox[4].add(board[row][col])
                        else:
                            return False

                    if 3 <= row <= 5 and 6 <= col <= 8:
                        if board[row][col] not in hmBox[5]:
                            hmBox[5].add(board[row][col])
                        else:
                            return False

                    if 6 <= row <= 8 and 0 <= col <= 2:
                        if board[row][col] not in hmBox[6]:
                            hmBox[6].add(board[row][col])
                        else:
                            return False

                    if 6 <= row <= 8 and 3 <= col <= 5:
                        if board[row][col] not in hmBox[7]:
                            hmBox[7].add(board[row][col])
                        else:
                            return False
                    
                    if 6 <= row <= 8 and 6 <= col <= 8:
                        if board[row][col] not in hmBox[8]:
                            hmBox[8].add(board[row][col])
                        else:
                            return False

        return True









