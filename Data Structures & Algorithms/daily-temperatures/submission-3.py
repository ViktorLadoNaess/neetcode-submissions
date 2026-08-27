class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res = [0 ]*len(temperatures)

        r =0
        while r<len(temperatures):
            while stack and temperatures[stack[-1]]<temperatures[r]:
                i = stack.pop()
                res[i]=r-i
            stack.append(r)
            r +=1

        return res