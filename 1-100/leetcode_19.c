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
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    struct ListNode* q = p,* h = p;
    int i = 0;
    while(i < n)
    {
        q = q->next;
        i++;
    }
    while(q->next != NULL)
    {
        q = q->next;
        h = h->next;
    }
    h->next = h->next->next;
    return p->next;
}



















