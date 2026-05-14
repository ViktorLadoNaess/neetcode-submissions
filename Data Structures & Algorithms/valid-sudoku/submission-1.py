class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(board):
            
            for row in board[:]:
                seen = set()
                for i in row:
                    if i in seen and i != ".":
                        return False
                    else:
                        seen.add(i)
            return True


        def checkCol(board,col_num):
            seen = set()
            for row_num in range(9):
                value =board[row_num][col_num]
                if value in seen and value != ".":
                    return False
                else:
                    seen.add(value)
            return True


        def miniBox(board):
            splices = [0,3,6,9]
            for col_lower, col_upper in zip(splices[:2],splices[1:]):
                for row_lower, row_upper in zip(splices[:2],splices[1:]):
                    seen = set()
                    for i in range(row_lower, row_upper):
                        for j in range(col_lower, col_upper):
                            value =board[i][j]
                            if value in seen and value != ".":
                                return False
                            else:
                                seen.add(value)
            return True
        if checkRow(board) == False:
            return False
        
        for col in range(9):
            if not checkCol(board,col):
                return False

        if miniBox(board) == False:
            return False
        
        return True





