""" 
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1 if (divisor < 0) is (dividend < 0) else -1
        print(f'\n----- dividend={dividend}, divisor={divisor}  --> sign={sign} -----')
        did, dis = abs(dividend), abs(divisor)
        while did >= dis:
            temp, i = dis, 1
            print(f'>> remain={did},\t res={res}')
            while did >= temp:
                print(f'    >> divisor={temp},\t quotient={i},\t remain={did - temp}')
                did -= temp
                res += i
                i <<= 1     # i += i        二進位左移符，相當於*2
                temp <<= 1  # temp += temp
        return min(max((res * sign), -pow(2, 31)), (pow(2, 31) - 1))

""" 
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -pow(2, 31) and divisor == -1:
            return pow(2, 31) - 1
        
        sign = 2
        if dividend > 0:
            dividend = -dividend
            sign -= 1
        if divisor > 0:
            divisor = -divisor
            sign -= 1

        max_bit = 0
        while divisor >= -pow(2, 30) and divisor + divisor >= dividend:
            max_bit += 1
            divisor += divisor
        
        res = 0
        for i in range(max_bit, -1, -1):
            if divisor >= dividend:
                res -= (1 << i)
                dividend -= divisor
            divisor = (divisor + 1) >> 1
        
        return -res if sign != 1 else res


    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = -1 if (divisor * dividend) < 0 else 1
        did, dis = abs(dividend), abs(divisor)
        while did >= dis:
            did -= dis
            res += 1
        return min(max((res * sign), -pow(2, 31)), (pow(2, 31) - 1))
     """

ans = [
    # {'dividend':10, 'divisor':3},
    # {'dividend':7, 'divisor':-3},
    {'dividend':100, 'divisor':9}
]
for trails in ans:
    print(Solution().divide(**trails))
