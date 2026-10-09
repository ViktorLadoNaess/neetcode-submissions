class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(len(numbers)):
            t = target- numbers[i]
            if t in seen:
                return [seen[t]+1,i+1]
            seen[numbers[i]]=i
                
     