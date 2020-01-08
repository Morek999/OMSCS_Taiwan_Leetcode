# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        buy = prices[0]
        profit = 0
        for i in prices:
            if i < buy:
                buy = i
            else:
                if (i - buy) > profit:
                    profit = i - buy
        return profit


ans = [
    [7,1,5,3,6,4],
    [7,6,4,3,1],
    [6,2,7,1,4,5],
    [6,2,3,1,4,5]
]
for trails in ans:
    print(Solution().maxProfit(trails))
