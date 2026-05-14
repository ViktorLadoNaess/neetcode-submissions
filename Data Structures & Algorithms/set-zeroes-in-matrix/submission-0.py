class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        zerod_rows = set()
        zerod_cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zerod_rows.add(i)
                    zerod_cols.add(j)
        for i in range(n):
            for j in range(m):
                if i in zerod_rows or j in zerod_cols:
                    matrix[i][j] = 0

                
        