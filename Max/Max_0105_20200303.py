""" 
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_idx = 0
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        def helper(left=0, right=len(inorder)):
            nonlocal pre_idx
            if left == right:
                return None
            val = preorder[pre_idx]
            root = TreeNode(val)
            index = idx_map[val]
            
            pre_idx += 1
            root.left = helper(left, index)
            root.right = helper(index + 1, right)
            return root
        return helper()

