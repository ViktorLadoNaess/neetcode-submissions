class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten_locations = []
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_locations.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        def dfs(t):
            nonlocal rotten_locations, fresh
            tmp = []
            for i, j in rotten_locations:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        tmp.append((ni, nj))
                        grid[ni][nj] = 2
                        fresh -= 1
            rotten_locations = tmp
            if len(tmp) == 0:
                return t if fresh == 0 else -1
            return dfs(t + 1)

        return dfs(0)