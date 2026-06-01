class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, i):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            val = board[r][c]

            if val == "#":
                return False

            if word[i] != val:
                return False

            if i == len(word) - 1:
                return True

            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            board[r][c] = val

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False