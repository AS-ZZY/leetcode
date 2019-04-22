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
bool hasCycle(struct ListNode *head) {
    if(head == NULL)
        return false;
    struct ListNode * p = head,* q = head;
    while(p->next != NULL&&p->next->next != NULL)
    {
        p = p->next->next;
        q = q->next;
        if(p == q)
            return true;
    }
    return false;
}






