""" 
50. Pow(x, n)
https://leetcode.com/problems/powx-n/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        curr = x
        i = n
        while i > 0:
            if (i % 2) == 1:
                ans *= curr
            curr *= curr
            i = i // 2
        return ans


ans = [
    {'x':2.0, 'n':10},  # 1024.0
    {'x':2.1, 'n':3},   # 9.261
    {'x':2.0, 'n':-2}   # 0.25
]
for trails in ans:
    print(Solution().myPow(**trails))
