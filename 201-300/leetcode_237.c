#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int main()
{
    return 0;
}

void deleteNode(struct ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
}

