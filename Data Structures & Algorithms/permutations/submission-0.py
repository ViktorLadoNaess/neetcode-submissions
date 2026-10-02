class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        curr = []

        def backtrack():
            if len(nums)==len(curr):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack()
                    curr.pop()
        backtrack()
        return res