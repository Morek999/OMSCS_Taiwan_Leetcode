/*
       1
     /   \
    2     3
   / \   / \
  4   5 6   7

pre: root, (left), (right): 1,2,4,5,3,6,7
In: (left), root, (right):  4,2,5,1,6,3,7
Pos:(left), (right), root:  4,5,2,6,7,3,1

(4,2,5),1,(6,3,7) ---> 1 is the root
   (4) 2 (5) -- > 2 is the root,       (6),3,(7) ---> 3 is the root
   (4) , (5) , (6) and (7) is the base 

Construct Binary Tree from Preorder and Inorder Traversal
So the idea is that can find the root from preorder in inorder sequence then separate the in order seqeuence into 2 parts: 
left subtree and right subtree
do the search recursively and construct the tree

*/

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return create(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);
    }

    TreeNode* create(vector<int>& preorder, vector<int>& inorder, int ps, int pe, int is, int ie){
                                                                                // search range
    if(ps > pe){
        return nullptr;
    }
    TreeNode* node = new TreeNode(preorder[ps]);
    int pos;
    // find the root location in the inorder sequence and than devide the sequence to
    // left to right    
    for(int i = is; i <= ie; i++){
        if(inorder[i] == node->val){
            pos = i;
            break;
        }
    }
    // length of the left subtree will be pos - is
    node->left = create(preorder, inorder, ps + 1, ps + pos - is, is, pos - 1);
    // length of the right subtree will be ie - pos
    node->right = create(preorder, inorder, pe - (ie - pos) + 1, pe, pos + 1, ie);
    return node;
    }
};