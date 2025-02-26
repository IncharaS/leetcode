class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        slow = 0
        max_ = 0
        for fast in range(1, len(prices)):
            if prices[fast] - prices[slow] > max_:
                max_ =  prices[fast] - prices[slow]
            elif prices[fast] < prices[slow]:
                slow = fast
        return max_
        
