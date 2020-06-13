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
    if (n == 0 || n == 1) {
        return 1;
    }
    int a = 1, b = 1;
    for (int i = 2; i <= n; i++) {
        b = a + b;
        a = b - a;
    }
    return b;
}



















