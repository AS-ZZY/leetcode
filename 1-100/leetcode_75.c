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
void sortColors(int* nums, int numsSize) {
    int i,j = 0,k = numsSize - 1;
    for(i = 0;i < k + 1;)
    {
        if(nums[i] == 0)
        {
            nums[j] = 0;
            j++;
            i++;
        }
        else if(nums[i] == 2)
        {
            nums[i] = nums[k];
            nums[k] = 2;
            k--;
        }
        else
            i++;
    }
    for(i = j;i <= k;i++)
        nums[i] = 1;
}






