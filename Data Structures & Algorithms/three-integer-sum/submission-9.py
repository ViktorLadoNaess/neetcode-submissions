class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        print(nums)
        res =[]
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]+nums[i]==0:
                    if [nums[l],nums[r],nums[i]] not in res:
                        res.append([nums[l],nums[r],nums[i]])
                    l +=1
                    r -=1
                elif nums[l]+nums[r]+nums[i]<0:
                    l +=1
                else:
                    r -=1
        return res

