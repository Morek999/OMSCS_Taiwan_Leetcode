""" 
166. Fraction to Recurring Decimal
https://leetcode.com/problems/fraction-to-recurring-decimal/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not denominator: 
            return ''
        digi, remd = divmod(abs(numerator), abs(denominator))
        sign = '-' if (numerator * denominator < 0) else ''
        if remd == 0:
            return sign + str(digi)
        res = [sign + str(digi), '.']
        stack = []
        while remd not in stack:
            stack.append(remd)
            digi, remd = divmod((remd * 10), abs(denominator))
            res.append(str(digi))
        res.insert(stack.index(remd) + 2, '(')
        res.append(')')
        return ''.join(res).replace('(0)', '')
        

ans = [
    {'numerator':1, 'denominator':2},  # output = 0.5
    {'numerator':0, 'denominator':3},  # output = 0.5
    {'numerator':2, 'denominator':7},  # output = 0.(6)
]

for trails in ans:
    print(Solution().fractionToDecimal(**trails))
