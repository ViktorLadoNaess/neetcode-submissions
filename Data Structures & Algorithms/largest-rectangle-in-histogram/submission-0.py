class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lbars = [0] * n
        rbars = [0] * n
        mbar = 0

        # distance to first smaller bar on the left
        for i in range(n):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= lbars[j]
            lbars[i] = i - j

        # distance to first smaller bar on the right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n and heights[j] >= heights[i]:
                j += rbars[j]
            rbars[i] = j - i

        for i in range(n):
            width = lbars[i] + rbars[i] - 1
            mbar = max(mbar, heights[i] * width)

        return mbar