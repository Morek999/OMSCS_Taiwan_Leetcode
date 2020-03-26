""" 
38. Count and Say
https://leetcode.com/problems/count-and-say/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        return ''.join(self.nextSeq(n, ['1', 'E']))
    
    def nextSeq(self, n, prev):
        if n == 1: return prev[:-1]
        new = []
        temp = prev[0]
        cnt = 1
        for i in prev[1:]:
            if i == temp:
                cnt += 1
            else:
                new.extend([str(cnt), temp])
                temp = i
                cnt = 1
        new.append('E')
        return self.nextSeq(n-1, new)


ans = [     
    # 1,  # 1
    4   # 1211
]
for trails in ans:
    print(Solution().countAndSay(trails))
