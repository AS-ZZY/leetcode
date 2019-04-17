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
int trailingZeroes(int n) {
    int a = 0;
    while(n > 0)
    {
        a += n / 5;
        n /= 5;
    }
    return a;
}



















