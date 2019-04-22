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
struct ListNode* oddEvenList(struct ListNode* head) {
    if(head == NULL|| head->next == NULL)
        return head;
    struct ListNode* p = head;
    struct ListNode* q = head->next;
    while(q->next != NULL)
    {
        struct ListNode* k = q->next;
        q->next = k->next;
        k->next = p->next;
        p->next = k;
        p = p->next;
        if(q->next == NULL)
            break;
        else
            q = q->next;
    }
    return head;
}














