class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        fin = []
        def dfs(start, res, t):
            if t == 0:
                fin.append(res)
                return

            if t < 0:
                return

            for i in range(start, len(nums)):
                dfs(i, res + [nums[i]], t - nums[i])
        dfs(0, [], target)
        return fin