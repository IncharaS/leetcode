class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        lo = 0
        hi = 0
        profit = 0
        i = 0
        n = len(prices)
        while i < n-1:

            ##when to buy, move till todays price is still greater than tomorrows
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            lo = prices[i]

            ##when to sell, move till todays price is lesser than tomorrows
            while i< n-1 and prices[i] <= prices[i+1]:
                i += 1
            hi = prices[i]
            profit += hi - lo
        return profit
        