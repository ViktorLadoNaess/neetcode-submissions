class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 1  # virtual empty plot before the start
        res = 0
        for space in flowerbed:
            if space == 0:
                c += 1
                if c == 3:
                    res += 1
                    c = 1
            else:
                c = 0
        if c == 2:  # virtual empty plot after the end
            res += 1
        return res >= n
