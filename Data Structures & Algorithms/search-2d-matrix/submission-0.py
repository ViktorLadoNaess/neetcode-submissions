class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full = []
        for row in matrix:
            full.extend(row)
        print(full)
        l = 0
        r = len(full)-1
        while l <=r:
            mid = (l+r)//2
            if full[mid]== target:
                return True
            elif full[mid]<= target:
                l = mid +1
            else:
                r = mid-1
        return False