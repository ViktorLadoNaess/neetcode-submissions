class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        left = 0
        right = n - 1

        while left < right:
            for i in range(right - left):
                top = left
                bottom = right

                # save top-left
                temp = matrix[top][left + i]

                # bottom-left -> top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom-right -> bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top-right -> bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # temp/top-left -> top-right
                matrix[top + i][right] = temp

            left += 1
            right -= 1