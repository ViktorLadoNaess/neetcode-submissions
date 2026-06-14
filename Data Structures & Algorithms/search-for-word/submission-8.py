class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c,i):
            if r<0 or r>= rows or c <0 or c >= cols:
                return False
            val = board[r][c]
            if val != word[i]:
                return False
            i +=1
            if i == len(word):
                return True
            board[r][c] = '#'
            res = dfs(r+1,c,i) or dfs(r-1,c,i) or dfs(r,c+1,i) or dfs(r,c-1,i)
            board[r][c] = val
            return res
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0)==True:
                    return True

        return False
            