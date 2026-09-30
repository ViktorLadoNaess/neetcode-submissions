class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        d ={}
        i = len(nums2)-1
        while i >=0:
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                d[nums2[i]]=stack[-1]
            else: 
                d[nums2[i]]=-1
            stack.append(nums2[i])
            i-=1
        return [d[val] for val in nums1]