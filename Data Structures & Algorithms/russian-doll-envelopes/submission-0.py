from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))

        tails = []

        for width, height in envelopes:
            position = bisect_left(tails, height)

            if position == len(tails):
                tails.append(height)
            else:
                tails[position] = height

        return len(tails)