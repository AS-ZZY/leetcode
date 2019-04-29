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
bool hasPathSum(struct TreeNode* root, int sum){
    if(root == NULL)
        return false;
    int a = sum - root->val;
    if((a == 0) && (root->left == NULL && root->right == NULL))
        return true;
    return hasPathSum(root->left,a) || hasPathSum(root->right, a);
}






