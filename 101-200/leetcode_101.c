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
bool is_same(struct TreeNode* p,struct TreeNode* q);
bool isSymmetric(struct TreeNode* root) {
    if(root == NULL)
        return true;
    return is_same(root->left, root->right);
}
bool is_same(struct TreeNode* p,struct TreeNode* q)
{
    if(p == NULL && q == NULL)
        return true;
    if(p == NULL || q == NULL)
        return false;
    if(p->val == q->val)
        return is_same(p->left,q->right) && is_same(p->right.q->left);
    return false;
}






