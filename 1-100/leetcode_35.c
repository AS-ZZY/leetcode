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
int searchInsert(int* nums, int numsSize, int target) {
    int i;
    for(i = 0;i < numsSize;i++)
    {
        if(target <= nums[i])
            break;
    }
    return i;
}













