
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprice = 0

        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprice:
                maxprice = price - minprice

        return maxprice
