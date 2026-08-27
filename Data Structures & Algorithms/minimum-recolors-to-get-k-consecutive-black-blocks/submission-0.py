class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m = float('inf') 
        ws= 0
        bs=0 
        l = 0
        r= 0
        while r in range(len(blocks)):
            if blocks[r]=='W':
                ws +=1
            else:
                bs +=1
            if ws +bs == k :
                m = min(m,ws)
                while l<r and ws+bs ==k:
                    m = min(m,ws)
                    if blocks[l]=='W':
                        ws-=1
                    else:
                        bs -=1
                    l +=1
            r+=1 
        return m
            
