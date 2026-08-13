class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0]*n for _ in range(n)]
        val = 1
        rmin, rmax, cmin, cmax = 0, n, 0, n
        r = c = 0

        while val <= n*n:
            # right along top row
            r, c = rmin, cmin
            while c < cmax:
                grid[r][c] = val
                val += 1
                c += 1
            rmin += 1

            # down right column
            r, c = rmin, cmax - 1
            while r < rmax:
                grid[r][c] = val
                val += 1
                r += 1
            cmax -= 1

            # left along bottom row
            r, c = rmax - 1, cmax - 1
            while c >= cmin:
                grid[r][c] = val
                val += 1
                c -= 1
            rmax -= 1

            # up left column
            r, c = rmax - 1, cmin
            while r >= rmin:
                grid[r][c] = val
                val += 1
                r -= 1
            cmin += 1

        return grid