""" 
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        if n == 0: return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]
        left = self.getSkyline(buildings[: (n//2)])
        right = self.getSkyline(buildings[(n//2): ])
        return self.merge(left, right)
    
    def merge(self, left, right):
        def update_output(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] = y
        def append_skyline(p, lst, n, y, curr):
            while p < n:
                x, y = lst[p]
                p += 1
                if curr != y:
                    update_output(x, y)
                    curr = y
        
        nL, nR = len(left), len(right)
        pL = pR = 0
        curr = yL = yR = 0
        output = []
        while (pL < nL) and (pR < nR):
            if left[pL][0] < right[pR][0]:
                x, yL = left[pL]
                pL += 1
            else:
                x, yR = right[pR]
                pR += 1
            yMax = max(yL, yR)
            if curr != yMax:
                update_output(x, yMax)
                curr = yMax
        append_skyline(pL, left, nL, yL, curr)
        append_skyline(pR, right, nR, yR, curr)
        return output


ans = [
    [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
]
for trails in ans:
    print(Solution().getSkyline(trails))
