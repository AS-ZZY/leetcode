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
int removeDuplicates(int* nums, int numsSize) {
    int i = 1;j = 1;
    if(numsSize == 0)
        return 0;
    for(;i < numsSize;i++)
    {
        if(nums[i] != nums[j - 1])
        {
            nums[j] = nums[i];
            j++;
        }
    }
    return j;
}













