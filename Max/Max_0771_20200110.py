""" 
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/
Time complexity: O(J+S)
Space complexity: O(S)
Solution: Store listed J to reduce the time complexity.
 """

from typing import List
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        J_list = list(J)
        for i in list(S):
            cnt += (i in J_list)
        return cnt

ans = [
    {'J':"aA", "S":"aAAbbbb"},
    {'J':"z", "S":"ZZ"}
]
for trails in ans:
    print(Solution().numJewelsInStones(trails))
