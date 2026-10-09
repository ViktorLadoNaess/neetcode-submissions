class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set(s[0])
        l = 0
        r = 0
        m =0
        while r <len(s):
            if s[r] not in seen:
                seen.add(s[r])
                
            else:
                while l<r and s[r] in seen:

                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            r +=1
            m = max(m,len(seen))

        return max(m,len(seen))




            