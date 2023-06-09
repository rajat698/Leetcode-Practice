class Solution:
    def maxProfit(self, prices) -> int:

        s = len(prices)
        prices.append(0)
        l, r = 0, 0
        totalProfit = 0
        currentTotal = 0

        while r < s:

            if prices[r] < prices[l]:
                l = r
    
            elif prices[l] < prices[r]:
                currentTotal = max(currentTotal, prices[r] - prices[l])
    
            if prices[r] > prices[r + 1]:
                totalProfit += currentTotal
                l = r
                currentTotal = 0
    
            r += 1
        
        return max(currentTotal, totalProfit)