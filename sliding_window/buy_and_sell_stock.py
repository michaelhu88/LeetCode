import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = math.inf
        difference = 0

        for price in prices:
            difference = max(price-min_so_far, difference)
            min_so_far = min(min_so_far, price)
        
        return difference