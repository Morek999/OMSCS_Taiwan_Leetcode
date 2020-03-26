""" 
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        for i in tokens:
            if i in op:
                b = stack.pop()
                a = stack.pop()
                oper = op[i]
                stack.append(oper(a, b))
            else:
                stack.append(int(i))
            print(f'{i}: {stack}')
        return stack.pop()
        

ans = [     
    # ["2", "1", "+", "3", "*"],      # 9
    # ["4", "13", "5", "/", "+"],     # 6
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]   # 22
]
for trails in ans:
    print(Solution().evalRPN(trails))
