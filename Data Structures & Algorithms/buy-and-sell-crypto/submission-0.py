class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit = prices[0]
        bestprofit =0
        for i in range(1, len(prices)):
            summ = prices[i] - minprofit 
            bestprofit = max(bestprofit, summ)
            minprofit = min(minprofit, prices[i])
        return bestprofit

        