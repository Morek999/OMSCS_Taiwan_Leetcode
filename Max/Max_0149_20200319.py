""" 
149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_a_line_containing_point_i(i):
            def add_line(i, j, count, duplicates):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 == x2 and y1 == y2:  
                    duplicates += 1
                elif y1 == y2:
                    nonlocal horisontal_lines
                    horisontal_lines += 1
                    count = max(horisontal_lines, count)
                else:
                    slope = (x1 - x2) / (y1 - y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)
                return count, duplicates
            
            lines, horisontal_lines = {}, 1
            count = 1
            duplicates = 0
            for j in range(i + 1, n):
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates
            
        n = len(points)
        if n < 3:
            return n
        
        max_count = 1
        for i in range(n - 1):
            max_count = max(max_points_on_a_line_containing_point_i(i), max_count)
        return max_count


ans = [
    [[1,1],[2,2],[3,3]],        # 3
    [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]   # 4
]
for trails in ans:
    print(Solution().maxPoints(trails))
