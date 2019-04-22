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
struct TreeNode* invertTree(struct TreeNode* root) {
    if(root == NULL)
        return NULL;
    struct TreeNode* p = root;
    p = root->left;
    root->left = root->right;
    root->right = p;
    invertTree(root->left);
    invertTree(root->right);
    return root;
}






