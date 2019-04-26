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
int rob(int* nums, int numsSize) {
    if(numsSize < 1)
        return NULL;
    int p1 = 0;
    int p2 = 0;
    int i = 0;
    for(i = 0;i < numsSize;i++)
    {
        if(i % 2 == 0)
        {
            if(p1 + nums[i] > p2)
                p1 += nums[i];
            else
                p1 = p2;
        }
        else
        {
            if(p2 + nums[i] > p1)
                p2 += nums[i];
            else
                p2 = p1;
        }
    }
    return p1 > p2 ? p1 : p2;
}





