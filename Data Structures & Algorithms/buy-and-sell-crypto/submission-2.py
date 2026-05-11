class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_l, max_r = 0, 0
        for l in range(len(prices)):
            for r in range(l, len(prices)):
                if prices[r] - prices[l] > profit:
                    max_l, max_r = l, r
                    profit = prices[r] - prices[l]
        return profit