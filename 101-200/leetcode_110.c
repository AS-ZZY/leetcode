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
int l(struct TreeNode* root);
bool isBalanced(struct TreeNode* root) {
    if(root == NULL)
        return true;
    else
    {
        int a=l(root->left);
        int b=l(root->right);
        if(a==b||a==b+1||a==b-1)
            return isBalanced(root->left)&&isBalanced(root->right);
        else
            return false;
    }
}
int l(struct TreeNode* root)
{
    if(root == NULL)
        return 0;
    else
    {
        int a=l(root->left);
        int b=l(root->right);
        return 1+(a>b?a:b);
    }
}





