class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest= 0
        seen = set()
        for l in range(len(s)):
            r = l
            while r < len(s):
                if s[r] in seen:
                    seen = set()
                    break
                else: 
                    seen.add(s[r])
                    r+=1 
            longest = max(r-l,longest)
        return longest
            

                             

            


                        
        