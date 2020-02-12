""" 
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
Time complexity: O()
Space complexity: O()
Solution: https://www.youtube.com/watch?v=n_yl2a6n7nM
 """

from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        neigh = defaultdict(set)
        for dest, src in prerequisites:
            dic[dest].add(src)
            neigh[src].add(dest)
        stack = [i for i in range(numCourses) if not dic[i]]
        print(f' dic = {dic} \n neigh = {neigh} \n stack = {stack} \n----')
        topo_order = []
        while stack:
            node = stack.pop()
            topo_order.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
            print(f' node = {node} \n dic = {dic} \n neigh = {neigh} \n stack = {stack} \n topo = {topo_order} \n----')
        return topo_order if not dic else []
    """ 
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        for dest, src in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            adj_list[src].append(dest)
        topo_order = []
        possible = True
        color = {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal possible
            if not possible: return
            color[node] = Solution.GRAY
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        possible = False
            color[node] = Solution.BLACK
            topo_order.append(node)
        
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        return topo_order[::-1] if possible else []
 """

ans = [
    # {'numCourses': 2, 'prerequisites': [[1,0]]},        # output: [0,1]
    {'numCourses': 4, 'prerequisites': [[1,0],[2,0],[3,1],[3,2]]}   # output: [0,1,2,3] or [0,2,1,3]
]
for trails in ans:
    print(Solution().findOrder(**trails))
