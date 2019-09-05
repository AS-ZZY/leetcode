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
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(head == NULL || head->next == NULL)
        return head;
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* q = p,* x;
    p->next = head;
    int i = 0;
    while(q->next != NULL)
    {
        q = q->next;
        i++;
    }
    k = k % i;
    if(k == 0)
        return head;
    q->next = head;
    q = p;
    k = i - k;
    while(k > 0)
    {
        k--;
        q = q->next;
    }
    x = q->next;
    q->next =NULL;
    free(p);
    return x;
}



















