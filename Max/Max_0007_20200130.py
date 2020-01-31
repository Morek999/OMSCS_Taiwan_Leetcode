""" 
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        if x is None: return None
        if not(-pow(2,31) <= x <= pow(2,31)-1): return 0
        res = neg = ''
        for i in list(str(x)):
            if i == '-':
                neg = i
            else:
                res = i + res
        ans = int(neg + res) 
        return ans if (-pow(2,31) <= ans <= pow(2,31)-1) else 0
    
ans = [
    123,    # output = 321
    -123,   # output = -321
    120     # output = 21
]

for trails in ans:
    print(Solution().reverse(trails))
