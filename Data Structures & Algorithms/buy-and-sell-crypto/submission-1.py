class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        max_l, max_r = 0, 0
        for l in range(len(prices)):
            for r in range(l, len(prices)):
                print(prices[r] - prices[l])
                if prices[r] - prices[l] > profit:
                    max_l, max_r = l, r
                    profit = prices[r] - prices[l]
        print(max_l, max_r)
        return profit