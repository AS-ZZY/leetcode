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
int majorityElement(int* nums, int numsSize){
    int num = nums[0];
    int num_s = 1;
    for(int i = 1;i < numsSize;i++)
    {
        if(nums[i] == num)
            num_s++;
        else{
            num_s--;
            if (num_s < 0){
                num = nums[i];
                num_s = 1;
            }
        }
    }
    return num;
}






