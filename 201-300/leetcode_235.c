#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int main()
{
    return 0;
}
bool re(struct TreeNode* root, struct TreeNode* p);
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if(root == NULL)
        return false;
    struct TreeNode* a = root;
    while(re(a,p)&&re(a,q))
    {
        if(re(a->right, p)&&re(a->right, q))
            a = a->right;
        else if(re(a->left, p)&&re(a->left, q))
            a = a->left;
        else
            break;
    }
    return a;
}

bool re(struct TreeNode* root, struct TreeNode* p){
    if(root == NULL)
        return false;
    else if(root == p)
        return true;
    else
        return re(root->left, p)||re(root->right, p);
}
