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
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    struct ListNode* q = p;
    while(q->next != NULL && q->next->next != NULL)
    {
        struct ListNode* k = q->next->next;
        q->next->next = k->next;
        k->next = q->next;
        q->next = k;
        q = q->next->next;
    }
    q = p->next;
    free(p);
    return q;
}





