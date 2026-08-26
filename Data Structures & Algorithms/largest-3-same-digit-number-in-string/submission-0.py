class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = -1
        for i in range(2,len(num)):
            if num[i]==num[i-1]==num[i-2]:
                m = max(m,int(num[i]*3))
            
        if m == -1:
            return ''
        elif m==0:
            return '000'
        else: return str(m) 
