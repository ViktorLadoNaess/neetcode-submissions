class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxC= 0
        l = 0

        count={}
        res= 0
        for r in range(len(s)):
            # include s[r] in the window
            count[s[r]] = 1 + count.get(s[r], 0)
            # update max of old or if new count is larger in this window
            maxC = max(maxC, count[s[r]])

            while (r-l+1)-maxC>k: # (window size) – (frequency of most common char)
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
        

        