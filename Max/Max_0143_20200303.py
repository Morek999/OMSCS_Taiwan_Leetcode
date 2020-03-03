""" 
134. Gas Station
https://leetcode.com/problems/gas-station/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start
        
ans = [
    {'gas': [1,2,3,4,5], 'cost': [3,4,5,1,2]},  # 3
    {'gas': [2,3,4], 'cost': [3,4,3]}           # -1
]
for trails in ans:
    print(Solution().canCompleteCircuit(**trails))
