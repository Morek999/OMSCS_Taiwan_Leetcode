""" 
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root: 
                continue
            val = root.val
            if not (lower < val < upper):
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
