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
struct TreeNode* tree(int* num,int frist,int last);
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return tree(nums, 0, numsSize - 1);
}
struct TreeNode* tree(int* num,int frist,int last)
{
    struct TreeNode* p = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    if(frist == last)
    {
        p->val = num[last];
        p->left = NULL;
        p->right = NULL;
    }
    else if(last < frist)
    {
        return NULL;
    }
    else
    {
        int mid = (frist + last) / 2;
        p->val = num[mid];
        p->left = tree(num, frist,mid - 1);
        p->right =tree(num,mid + 1,last);
    }
    return p;
}

















