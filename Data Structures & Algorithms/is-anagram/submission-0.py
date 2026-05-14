class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s =dict()
        dic_t =dict()
        for i in range(len(s)):
            if (s[i] in dic_s) ==True:
                dic_s[s[i]] = dic_s[s[i]] + 1
            else:
                dic_s[s[i]] =1
            if (t[i] in dic_t) ==True:
                dic_t[t[i]] = dic_t[t[i]] + 1
            else:
                dic_t[t[i]] =1

        for i in range(len(s)):
            try:  
                if dic_s[s[i]] != dic_t[s[i]]:
                    return False
            except KeyError:
                return False
        return True
            
                
