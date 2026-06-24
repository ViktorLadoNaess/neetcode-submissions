class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r <0 or r >= rows or c <0 or c>= cols):
                return False
            val = board[r][c]
            if val == '#':
                return False
            if val != word[i]:
                return False
            board[r][c]='#'
            res = dfs(r+1,c,i+1)or dfs(r-1,c,i+1)or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=val
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0)== True:
                    return True

        return False
    
        