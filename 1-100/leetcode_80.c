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
int removeDuplicates(int* nums, int numsSize){
    int i,j;
    if(numsSize <= 2)
        return numsSize;
    for(i = 2,j = 2;i < numsSize;)
    {
        if(nums[i] == nums[j - 1] && nums[i] == nums[j - 2])
            i++;
        else
            nums[j++] = nums[i++];
    }
    return j;
}






