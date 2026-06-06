class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=''
        for n in digits:
            res+=f'{n}'
        print(res)
        res= int(res)+1
        res = str(res)
        r=[]
        for c in res:
            r.append(c)
        return r

