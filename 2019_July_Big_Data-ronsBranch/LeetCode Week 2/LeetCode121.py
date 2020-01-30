from _ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice=float("inf")
        profit=0
        for sellPrice in prices:
            if sellPrice-buyPrice>profit:
                profit=sellPrice-buyPrice
            if buyPrice>sellPrice:
                buyPrice=sellPrice
        return profit