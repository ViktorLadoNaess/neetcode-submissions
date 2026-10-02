class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_c =image[sr][sc]
        if orig_c == color:
            return image

        def dfs(r,c):
            if r<0 or r >= len(image):
                return
            if c<0 or c >= len(image[0]):
                return
            if image[r][c]!=orig_c:
                return 
            image[r][c]= color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        dfs(sr,sc)
        return image


            