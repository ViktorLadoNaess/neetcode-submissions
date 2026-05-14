class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        result_len = n*m
        result = []
        left_bound=0
        right_bound=m-1
        bottom_bound = n-1
        top_bound = 1
        i,j =0,0
        result.append(matrix[i][j])
        while len(result) != result_len:
            while j < right_bound:
                j +=1
                result.append(matrix[i][j])
            right_bound -=1    
            while i < bottom_bound:
                i +=1
                result.append(matrix[i][j])
            bottom_bound -=1
            if len(result) == result_len: break
            while j > left_bound:
                j -=1
                result.append(matrix[i][j])
            left_bound +=1    
            while i > top_bound:
                i -=1
                result.append(matrix[i][j])
            top_bound +=1
        return result
