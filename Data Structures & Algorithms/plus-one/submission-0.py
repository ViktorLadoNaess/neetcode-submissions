class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_dig= ''.join(str(x) for x in digits)
        print(str_dig)
        num=int(str_dig)
        num+=1
        num= str(num)
        result=[]
        for i in range(len(num)):
            result.append(num[i])
        return result