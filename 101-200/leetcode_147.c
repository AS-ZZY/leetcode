struct ListNode* insertionSortList(struct ListNode* head) {
    struct ListNode* l = (struct ListNode*)malloc(sizeof(struct ListNode));
    l->next = head;
    if(head == NULL)
        return NULL;
    struct ListNode* n = l->next;
    struct ListNode* p,* q;
    while(n->next != NULL)
    {
        p = l;
        q = n->next;
        if(q->val > n->val)
            n = n->next;
        else
        {
            while(p != n)
            {
                if(p->next->val < q->val)
                    p = p->next;
                else
                    break;
            }
            n->next = q->next;
            q->next = p->next;
            p->next = q;
        }
    }
    return l->next;
}