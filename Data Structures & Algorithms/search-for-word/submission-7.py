class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c, i ):
            if (r>= rows or r <0 or c >= cols or c <0):
                return False
            val = board[r][c]
            if val == '#':
                return False
            
            if val != word[i]:
                return False
            i +=1
            if i >=len(word): return True
            board[r][c] = '#'
            res= dfs(r+1,c, i) or dfs(r-1,c, i) or  dfs(r,c+1, i) or dfs(r,c-1, i)
            board[r][c] = val
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0) == True:
                    return True
        return False

