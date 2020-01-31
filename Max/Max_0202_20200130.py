""" 
202. Happy Number
https://leetcode.com/problems/happy-number/submissions/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def isHappy(self, n: int) -> bool:
        if n in [4, 16, 37, 58, 89, 145, 42, 20]: 
            return False
        res = 0
        for i in str(n):
            res += pow(int(i), 2)
        if res == 1:
            return True
        return self.isHappy(res)
    
ans = [
    19
]

for trails in ans:
    print(Solution().isHappy(trails))
