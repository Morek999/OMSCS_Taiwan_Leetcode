""" 
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
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

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def recur(node, lvl):
            if len(levels) == lvl:
                levels.append([])
            levels[lvl].append(node.val)
            if node.left:
                recur(node.left, lvl + 1)
            if node.right:
                recur(node.right, lvl + 1)
        
        recur(root, 0)
        return levels
