""" 
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        if not s: return 0
        s += '+0'
        stack = []
        hold = 0
        op = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                hold = hold * 10 + int(s[i])
            else:
                if   op == '-': stack.append(-hold)
                elif op == '+': stack.append(hold)
                elif op == '*': stack.append(stack.pop() * hold)
                else: stack.append(int(stack.pop() / hold))
                op ,hold = s[i], 0
        return sum(stack)


ans = [
    "3+2*2",   # output = 7
    " 3/2 ",    # output = 1
    " 3+5 / 2 ", # output = 5
    '42',
    "0-2147483647",
    "14-3/2",
    "1*2-3/4+5*6-7*8+9/10"
]
for trails in ans:
    print(Solution().calculate(trails))
