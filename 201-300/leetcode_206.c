#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
int main()
{
    return 0;
}
struct ListNode* reverseList(struct ListNode* head) {
    if(head == NULL||head->next == NULL)
        return head;
    struct ListNode* q = head->next,* l;
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p->next = head;
    p->next->next = NULL;
    while(q != NULL)
    {
        l = q->next;
        q->next = p->next;
        p->next = q;
        q = l;
    }
    return p->next;
}
