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

struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* q = (struct ListNode*)malloc(sizeof(struct ListNode));
    q->next= head;
    struct ListNode* p = q;
    while(p->next != NULL)
    {
        if(p->next->val == val)
        {
            struct ListNode* l;
            l = p->next;
            p->next = l->next;
            free(l);
        }
        else
            p = p->next;
    }
    p = q->next;
    free(q);
    return p;
}















