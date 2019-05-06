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
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* p = headA,* q = headB,* k;
    while(p != NULL && q != NULL)
    {
        p = p->next;
        q = q->next;
    }
    if(p == NULL)
    {
        k = headB;
        p = headA;
    }
    else
    {
        k = headA;
        q = p;
        p = headB;
    }
    while(q != NULL)
    {
        k = k->next;
        q = q->next;
    }
    while(k != NULL && k != p)
    {
        k = k->next;
        p = p->next;
    }
    return k;
}






