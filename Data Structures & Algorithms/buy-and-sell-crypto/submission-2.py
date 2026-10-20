class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprof=float('inf')
        maxprof=0
        for price in prices:
            if price<minprof:
                minprof=price
            elif maxprof<price-minprof:
                maxprof=price-minprof
        return maxprof
        