""" 
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -float('inf')
        def max_gain(node):
            nonlocal res
            if not node: return 0
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            price_new_path = node.val + left + right
            res = max(res, price_new_path)
            return node.val + max(left, right)
        max_gain(root)
        return res

