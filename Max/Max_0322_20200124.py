""" 
322. Coin Change
https://leetcode.com/problems/coin-change/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in coins:
            # print(f'>>> {i}')
            for x in range(i, amount + 1):
                dp[x] = min(dp[x], dp[x-i] + 1)
                # print(f'> {x}: {dp}')
        return dp[amount] if dp[amount] != float('inf') else -1
""" 
        if coins is None: return -1
        coins.sort(reverse=True)
        holding = {}
        remain = amount
        for i in coins:
            holding[i] = remain // i
            remain %= i
        return (sum(holding.values()) if remain == 0 else -1)
 """
    
ans = [
    {'coins':[1, 2, 5], 'amount':11},   # output = 3   (11=5+5+1)
    {'coins':[2], 'amount':3}           # output = -1
]

for trails in ans:
    print(Solution().coinChange(**trails))
