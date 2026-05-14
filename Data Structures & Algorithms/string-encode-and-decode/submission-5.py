class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=f"#{len(s)}#{s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i <len(s):
            i +=1
            j = i
            while s[j] != '#':
                j +=1
            s_len= int(s[i:j])
            print(s_len)
            w =s[j+1:j+s_len+1]
            print(w)
            i = j+s_len+1
            res.append(w)
        return res
