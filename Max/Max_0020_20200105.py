# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        holding = []
        ending = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in ending:
                if len(holding) == 0: return False
                if holding.pop() != ending[i]: return False
            else:
                holding.append(i)
        return len(holding) == 0

ans = [
    "()",
    '()[]{}',
    "(]",
    "([)]",
    "{[]}"
]
for trails in ans:
    print(Solution().isValid(trails))
