class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f'#{len(word)}#{word}'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i in range(len(s)):
            i +=1
            j = i 
            while s[j] != '#':
                j += 1 
            w_len= int(s[i:j])
            print(w_len)
            word = s[j+1:j+1+w_len]
            res.append(word)
            i = j+1+w_len

        return res