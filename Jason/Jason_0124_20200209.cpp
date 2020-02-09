/*

   -10
   / \
  9  20
    /  \
   15   7

Take this as example. Let's simplify the problem first. Suppose we write a function(MaxSum here) which takes a node as an argument and computes a maximum 
contribution that  this node and one/zero of its subtrees could add.

So the maximum gain from node 9 is 9, maximum gain for node 15 is 15 and maximum gain for node 7 is 7. The maximum gain from node 20 will be 
20 + max(MaxSum(15),MaxSum(7)) = 35. so the max gain from node -10 will be -10 + (MaxSum(9),MaxSum(20)) = 25

However, in this question, the path doesn't need to go through the root, and the answer to this question is 15 -> 20 -> 7 = 42

So in this question, we need to check at each step what is better : 
1. to continue the current path 
2. to start a new path with the current node as a highest node in this new path.

Implement Max_Sum(node) with a check to continue the old path/to start a new path:
#Base case : if node is null, the max gain is 0.
#Call MaxSum recursively for the node children to compute max gain from the left and right subtrees : 
  left_gain = max(MaxSum(node->left), 0) 
  right_gain = max(MaxSum(node->right), 0).
Now check to continue the old path or to start a new path. To start a new path would cost sum = node->val + left_gain + right_gain. 
Update max_sum if it's better to start a new path.
For the recursion return the max gain the node and one/zero of its subtrees could add to the current path : node.val + max(left_gain, right_gain).

Time complexity: O(n) since we need to traverse all of the element in the tree
Space complexity: O(log(n)) since we need to recursively call the function h times, where h is the binary tree height, which equals to log(n)
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        if(!root){
            return 0;
        }
        int ans = INT_MIN;
        MaxSum(root, ans);
        return ans;
    }
private:
    int MaxSum(TreeNode*root, int& ans){
        if(!root){
            return 0;
        }
        int l = max(0,MaxSum(root->left, ans));
        int r = max(0,MaxSum(root->right, ans));
        int sum = l + r + root->val;
        ans = max(ans, sum);
        return max(l,r) + root->val;
    }
};