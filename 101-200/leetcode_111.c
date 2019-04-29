#include <stdio.h>
#include <stdlib.h>
#define bool int
#define false 0
#define true 1
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct ListNode {
    int val;
    struct ListNode *next;
 };
int main()
{
    return 0;
}
int minDepth(struct TreeNode* root){
    if(root == NULL)
        return 0;
    if(root->right == NULL && root->left == NULL)
        return 1;
    else if(root->right == NULL && root->left != NULL)
        return 1 + minDepth(root->left);
    else if(root->right != NULL && root->left == NULL)
        return 1 + minDepth(root->right);
    else{
        int a = minDepth(root->left);;
        int b = minDepth(root->right);;
        return 1 + (a < b ? a : b);
    }
}






