class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left = 0
        right = n-1
        while left <= right:
            for i in range(right-left):
                top = left
                bottom = right
                #store top left
                tmp=matrix[top][left+i]
                matrix[top][left+i]=matrix[bottom-i][left] 
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right]= tmp
            
            left +=1
            right -=1
        return
