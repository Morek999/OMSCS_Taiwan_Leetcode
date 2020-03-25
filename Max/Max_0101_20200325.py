""" 
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
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
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(node1, node2):
            if (node1 is None) and (node2 is None):
                return True
            if (node1 is None) or (node2 is None):
                return False
            return (node1.val == node2.val) and isMirror(node1.right, node2.left) and isMirror(node1.left, node2.right)
        return isMirror(root, root)