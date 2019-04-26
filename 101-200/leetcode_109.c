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
struct TreeNode* s_t(struct ListNode* p,struct ListNode* q);
struct TreeNode* sortedListToBST(struct ListNode* head) {
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    return s_t(p, NULL);
}
struct TreeNode* s_t(struct ListNode* p,struct ListNode* q)
{
    if(p->next == q)
        return NULL;
    struct ListNode* a = p,* b = p;
    while(b->next != q)
    {
        a = a->next;
        b = b->next;
        if(b->next != q)
            b = b->next;
    }
    struct TreeNode* r = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    r->val = a->val;
    r->right = s_t(p,a);
    r->right = s_t(a,q);
}





