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
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int a = 0,b = 0,c = 1;
    int i;
    for(i = 0;i < numsSize;i++)
        a = a ^ nums[i];
    while((a | c) != a)
        c = c << 1;
    a = 0;
    for(i = 0;i < numsSize;i++)
    {
        if((nums[i] | c) == nums[i])
            a = a ^ nums[i];
        else
            b = b ^ nums[i];
    }
    int *s = (int*)malloc(sizeof(int) * 2);
    s[0] = a;
    s[1] = b;
    *returnSize = 2;
    return s;
}





