from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        q = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    num_fresh +=1
                elif grid[r][c]==2:
                    q.append([r,c])
        mins=0
        while num_fresh != 0:
            tmp = num_fresh
            nrf= len(q)
            for _ in range(len(q)):
                curr = q.popleft()
                r,c = curr[0],curr[1]
                for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr = r + i
                    nc = c + j

                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                        
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        num_fresh-=1
                        q.append([nr,nc])
    
            if num_fresh == tmp:
                return -1
            mins+=1
        return mins
