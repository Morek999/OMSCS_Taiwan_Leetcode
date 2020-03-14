""" 
204. Count Primes
https://leetcode.com/problems/count-primes/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2, n):
            if res[i]:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = 0
        return sum(res)

ans = [
    10
]
for trails in ans:
    print(Solution().countPrimes(trails))
