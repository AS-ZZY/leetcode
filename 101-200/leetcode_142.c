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
struct ListNode *detectCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL)
        return NULL;
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    struct ListNode* q = p->next,* k = q->next;
    while(k->next != NULL && k->next->next != NULL)
    {
        if(k == q)
            break;
        k = k->next->next;
        q = q->next;
    }
    if(k != q)
        return NULL;
    k = p;
    while(k != q)
    {
        k = k->next;
        q = q->next;
    }
    free(p);
    return k;
}






