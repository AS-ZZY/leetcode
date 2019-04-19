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
int minMoves(int* nums, int numsSize) {
    int min = nums[0];
    for(i = 1;i < numsSize;i++)
        if(min > nums[i])
            min = nums[i];
    int sum = 0;
    for(i = 0;i < numsSize;i++)
        sum += (nums[i] - min);
    return sum;
}

















