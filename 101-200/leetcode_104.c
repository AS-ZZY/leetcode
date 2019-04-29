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
int maxDepth(struct TreeNode* root) {
    if(root == NULL)
        return 0;
    else
    {
        int a = maxDepth(root->right);
        int b = maxDepth(root->left);
        return 1 + (a > b ? a : b);
    }
}






