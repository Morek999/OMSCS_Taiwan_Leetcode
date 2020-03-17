""" 
207. Course Schedule
https://leetcode.com/problems/course-schedule/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0  for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if visit[i] == 1:   return True
            if visit[i] == -1:  return False
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j): return False
            visit[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

ans = [
    {'numCourses':2, 'prerequisites':[[1,0]]},
    {'numCourses':2, 'prerequisites':[[1,0],[0,1]]}
]
for trails in ans:
    print(Solution().canFinish(**trails))
