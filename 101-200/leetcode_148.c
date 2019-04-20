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
void sort(struct ListNode* frist,struct ListNode* last);
struct ListNode* sortList(struct ListNode* head) {
    struct ListNode* p  = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    sort(p,NULL);
    return p->next;
}
void sort(struct ListNode* frist,struct ListNode* last)
{
    if(frist->next == last)
        return;
    struct ListNode* q = frist->next,* l = q,* n;
    while(l->next != last)
    {
        if(l->next->val < q->val)
        {
            n = l->next;
            l->next = n->next;
            n->next = frist->next;
            frist->next = n;
        }
        else
            l = l->next;
    }
    sort(frist, q);
    sort(q,last);
}














