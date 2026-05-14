class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ltrs= set()
        maxLen=0
        n= len(s)
        l = 0
        for r in range(len(s)):
            if s[r] in ltrs:
                
                while s[r] in ltrs:
                    ltrs.remove(s[l])
                    l +=1
                
            ltrs.add(s[r])
            maxLen=max(maxLen, r-l+1)
        return maxLen
            


                        
        