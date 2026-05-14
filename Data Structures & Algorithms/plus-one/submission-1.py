class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums_str=''.join(str(n) for n in digits)
        print(nums_str)
        nums = int(nums_str)
        nums +=1
        res= []
        for i in str(nums):
            res.append(int(i))
        return res