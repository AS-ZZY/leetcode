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
struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    int i = 1;
    struct ListNode* q = p,* l,* a;
    while(i < m)
    {
        i++;
        q = q->next;
    }
    l = q->next;
    i++;
    while(i < n)
    {
        i++;
        a = l->next;
        l->next = a->next;
        a->next = q->next;
        q->next = a;
    }
    q = p->next;
    free(p);
    return q;
}

















