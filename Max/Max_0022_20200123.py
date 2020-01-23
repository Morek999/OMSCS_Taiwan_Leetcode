""" 
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n is None: return None
        if n == 0: return ['']
        ans = []
        for i in range(n):
            for l in self.generateParenthesis(i):
                for r in self.generateParenthesis(n - 1 - i):
                    ans.append(f'({l}){r}')
        return ans
    
ans = [
    1,
    2,
    3
]

for trails in ans:
    print(Solution().generateParenthesis(trails))
