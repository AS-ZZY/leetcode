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
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* p = head;
    if(head == NULL)
        return NULL;
    while(p->next != NULL)
    {
        if(p->val == p->next->val)
        {
            struct ListNode* q = p->next;
            p->next = q->next;
            free(q);
        }
        else
            p = p->next;
    }
    return head;
}



















