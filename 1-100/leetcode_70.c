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

int climbStairs(int n) {
    int l1 = 0,l2 = 1,a;
    int i = 1;
    while(i <= n)
    {
        a = l2;
        l2 = l1 + l2;
        l1 = a;
        i++;
    }
    return l1;
}



















