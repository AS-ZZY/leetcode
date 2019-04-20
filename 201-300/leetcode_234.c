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

bool isPalindrome(struct ListNode* head) {
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* q = p,*l = p,* k;
    int a = 0;
    p->next = head;
    if(head == NULL || head->next == NULL)
        return true;
    while(q->next != NULL)
    {
        l = l->next;
        q = q->next;
        if(q->next != NULL)
            q = q->next;
        else
        {
            a = 1;
            break;
        }
    }
    k = l->next;
    l = head;
    while(l->next != k)
    {
        q = l->next;
        l->next = q->next;
        q->next = p->next;
        p->next = q;
    }
    q = p->next;
    if(a == 1)
        q = q->next;
    while(k != NULL)
    {
        if(k->val != q->val)
            return false;
        k = k->next;
        q = q->next;
    }
    return true;
}















