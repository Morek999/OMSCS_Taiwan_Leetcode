""" 
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Time complexity: O()
Space complexity: O()
Solution: 
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)

 """

from typing import List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def recur(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = recur(root.left, string)
                string = recur(root.right, string)
            return string
        return recur(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def recur(data_list):
            if data_list[0] == 'None':
                data_list.pop(0)
                return None
            root = TreeNode(data_list[0])
            data_list.pop(0)
            root.left = recur(data_list)
            root.right = recur(data_list)
            return root
        return recur(data.split(sep=','))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

ans = [
    {"s":"ADOBECODEBANC", "t":"ABC"}    # output: "BANC"
]
for trails in ans:
    print(Solution().minWindow(**trails))
