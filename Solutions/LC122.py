class Solution:
    def maxProfit(self, prices) -> int:

        totalProfit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:
                totalProfit += prices[i] - prices[i - 1]

        
        return totalProfit