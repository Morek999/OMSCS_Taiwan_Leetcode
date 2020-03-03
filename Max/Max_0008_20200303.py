""" 
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:     #### 36ms, 37% beat
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0: return 0
        res = '0'
        if str[0] == '-' or str[0] == '+':
            res = str[0] + res
            str = str[1:]
        for i in str:
            if i.isnumeric(): 
                res += i
                pos = True
            else:
                break
        return max(-pow(2, 31), min(pow(2, 31) - 1, int(res)))

class Solution:     #### 24ms, 97% beat
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str == '': return 0
        res = '0'
        neg = pos = False
        for i in str:
            if i.isnumeric():
                res += i
                pos = True
            elif (i == '-') and (not neg) and (not pos): 
                neg = True
            elif (i == '+') and (not neg) and (not pos):
                pos = True
            else:
                break
        res = -int(res) if neg else int(res)
        return max(-pow(2, 31), min(pow(2, 31) - 1, res))

ans = [
    "42",       # 42
    "   -42",       # -42
    "4193 with words",       # 4193
    "words and 987",        # 0
    "-91283472332",         # -2147483648
    "   +0 123",        # 0
    "0-1"               # 0
]
for trails in ans:
    print(Solution().myAtoi(trails))
