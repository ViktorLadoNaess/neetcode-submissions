class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ws = blocks[:k].count('W')
        m = ws
        for r in range(k,len(blocks)):
            ws += blocks[r]=='W'
            ws -= blocks[r-k]== 'W'
            m = min(ws,m)
        return m
