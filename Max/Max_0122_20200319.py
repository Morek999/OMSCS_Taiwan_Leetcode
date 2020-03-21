""" 
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


ans = [
    [7,1,5,3,6,4],  # 7
    [1,2,3,4,5],    # 4
    [7,6,4,3,1]     # 0
]
for trails in ans:
    print(Solution().maxProfit(trails))
