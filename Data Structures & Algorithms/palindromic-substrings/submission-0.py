class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l,r):
            count=0
            while l>=0 and r <len(s) and s[l]==s[r]:
                l -=1
                r+=1
                count+=1
            return count
        
        c = 0
        for i in range(len(s)):
            tc= expand(i,i)
            c +=tc
            tc = expand(i,i+1)
            c+=tc
        return c

                