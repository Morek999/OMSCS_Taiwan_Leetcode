""" 
412. Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            res = ''
            if (i + 1) % 3 == 0:
                res += 'Fizz'
            if (i + 1) % 5 == 0:
                res += 'Buzz'
            if res == '':
                res = str(i + 1)
            ans.append(res)
        return ans

ans = [
    15
]
for trails in ans:
    print(Solution().fizzBuzz(trails))
