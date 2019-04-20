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

int missingNumber(int* nums, int numsSize) {
    int i,a = 0;
    for(i = 0;i < numsSize;i++)
    {
        a = a ^ i ^nums[i];
    }
    a ^= numsSize;
    return a;
}
















