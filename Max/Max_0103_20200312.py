""" 
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Time complexity: O()
Space complexity: O()
 """

from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        res = []
        
        def dfs(node, level):
            if level >= len(res):
                res.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)
        dfs(root, 0)
        return res