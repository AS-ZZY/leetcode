#include <stdio.h>
#include <stdlib.h>
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

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if(p == NULL&&q == NULL)
        return true;
    else if(p == NULL||q == NULL)
        return false;
    else if(p->val == q->val)
        return true && isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
    return false;
}



















