""" 
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        seq = [self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]
        return root if all(seq) else max(v for v in seq if v is not None)

ans = [
    {'root': [3,5,1,6,2,0,8,None,None,7,4], 'p': 5, 'q': 1},      # output: 3
    {'root': [3,5,1,6,2,0,8,None,None,7,4], 'p': 5, 'q': 4}       # output: 5
]
for trails in ans:
    print(Solution().findOrder(**trails))
