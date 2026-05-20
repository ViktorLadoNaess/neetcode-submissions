class Solution:
    def rob(self, nums: List[int]) -> int:
        n_1 = 0
        n_2 = 0

        for n in nums:
            print(f"before: n={n}, n_1={n_1}, n_2={n_2}")

            curr = max(n_1, n_2 + n)
            n_2 = n_1
            n_1 = curr

            print(f"after: curr={curr}, n_1={n_1}, n_2={n_2}")

        return n_1