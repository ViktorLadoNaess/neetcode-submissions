class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr=[]

        def backtrack():
            if len(nums)==len(curr):
                res.append(curr.copy())
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack()
                    curr.pop()
        backtrack()
        return res